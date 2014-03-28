#!/bin/sh
#
### modified date: 2014/03/17
### nagios nsca command on backend 
#

NSCA_SERVER=k0.site
SEND_NSCA_CONF=/etc/nagios/send_nsca.cfg
HOST=`hostname`

#
### check job status
#
Check_Job_Status() {
DESCRIPTION="Job Status"
#Code   Status
#0      Ok
#1      Warning
#2      Critical
#Other  Unknown

STATUS=0
MESSAGE=""


# check g09
# don't implement
for CMD in `ps aux | awk '/\/usr\/local\/pkg\/g09/{print $11}'`; do
  EXE=${CMD##*/}
  MESSAGE="$MESSAGE, $EXE"
done
USER=`ps aux | awk "/\$EXE/{if (\\$8 ~ /R/) print \\$1}" | head -1`
RESULT="G09: CMD=$EXE, USER=$USER"



# check vasp
NPROC=0
for CMD in `ps aux | awk '/vasp/{if ($8 ~ /R/) print $11}'`; do
  EXE=${CMD##*/}
  MESSAGE="$MESSAGE, $EXE"
  NPROC=`expr $NPROC + 1`
done

#  USER=`ps aux | awk "/vasp/{if (\\$8 ~ /R/) print \\$1}" | head -1`
USER=`ps aux | awk "/\$EXE/{if (\\$8 ~ /R/) print \\$1}" | head -1`
#  RESULT="VASP: CMD=$EXE, NP=$NPROC USER=$USER"
RESULT="$RESULT; VASP: CMD=$EXE, NP=$NPROC USER=$USER"
#  echo $RESULT
  echo -e "$HOST\t$DESCRIPTION\t$STATUS\t$RESULT" | send_nsca -H $NSCA_SERVER -c $SEND_NSCA_CONF
}

#
### check Current Load
#
Check_Current_Load() {
  DESCRIPTION="Current Load"
  CMD=`/usr/lib/nagios/plugins/check_load -w 5.0,4.0,3.0 -c 10.0,6.0,4.0`
  STA=`echo $CMD | awk '{print $1}'`
  if [ "x$STA" ==  "xOK" ]; then
    STATUS=0
  elif [ "x$STA" ==  "xWARNING" ]; then
    STATUS=1
  elif [ "x$STA" ==  "xCRITICAL" ]; then
    STATUS=2
  else
    STATUS=3
  fi
  echo -e "$HOST\t$DESCRIPTION\t$STATUS\t$CMD" | send_nsca -H $NSCA_SERVER -c $SEND_NSCA_CONF
}

#
### check nsca command
#
Check_nsca_cmd() {
  DESCRIPTION=$1
  CMD=$2
  COLUMN=$3
#  STA=`echo $RESULT | awk '{print $1}'`
  RESULT="`$CMD`"
  STA=`echo $RESULT | awk "{print \\$$COLUMN}"`
  if [ "x$STA" ==  "xOK" ]; then
    STATUS=0
  elif [ "x$STA" ==  "xWARNING" ]; then
    STATUS=1
  elif [ "x$STA" ==  "xCRITICAL" ]; then
    STATUS=2
  else
    STATUS=3
  fi

  echo $HOST, $DESCRIPTION, $CMD, $RESULT, $NSCA_SERVER
  echo -e "$HOST\t$DESCRIPTION\t$STATUS\t$RESULT" | send_nsca -H $NSCA_SERVER -c $SEND_NSCA_CONF
}


#
### main
#

#Check_Current_Load

for I in `seq 5 `; do
  date
  echo "Run: $I"
  Check_nsca_cmd "Current Load" "/usr/lib/nagios/plugins/check_load -w 5.0,4.0,3.0 -c 10.0,6.0,4.0" 1
  Check_nsca_cmd "Root Partition" "/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /" 2
  Check_nsca_cmd "Tmp Partition" "/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /tmp" 2
  Check_nsca_cmd "Swap Usage" "/usr/lib/nagios/plugins/check_swap -w 20 -c 10" 2
  Check_nsca_cmd "Mount Point" "/usr/lib/nagios/plugins/check_mountpoints.sh /home /work /work2" 1
  Check_Job_Status
  sleep 10
done
