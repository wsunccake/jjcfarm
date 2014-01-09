#!/usr/bin/env sh 

exe_pidfile=exe.pid 
mon_pidfile=mon.pid 

# setup executable function 
exe() { 
     echo "exe begin: `date`"
     while true; do
        echo "exe.sh PID: $$  Hello, exe is still running" 
        sleep 10 
     done
     echo "exe finish: `date`"
} 

# setup monitor function 
mon() {
    echo "mon begin: `date`"
    monPID=$1 
    monPeriod=$2 
    monPeriod=${monPeriod:=5} 
    while true ;do 
        status=`ps -p $monPID -o pid| grep $monPID` 
        if [ -z $status ]; then 
            echo "Don't find PID: $monPID" 
            break 
        fi 

        echo "monitor $monPID" 
        ps -p $monPID 
        sleep $monPeriod 
    done 
    echo "mon finish: `date`"
} 

# setup kill mon and exe function 
killproc() { 
    pid1=`head -n1 $exe_pidfile` 
    echo "kill $pid1 prcoess" 
    kill -9 $pid1 
    rm $exe_pidfile 
    pid2=`head -n1 $mon_pidfile` 
    echo "kill $pid2 prcoess" 
    kill -9 $pid2 
    rm $mon_pidfile 
    exit 1 
} 


#
### main 
#

# run exe
exe&
exe_pid=$!
echo $exe_pid > $exe_pidfile 

# run mon
mon $exe_pid&
mon_pid=$!
echo $mon_pid > $mon_pidfile 

# trap signal
trap killproc 2

while [ 0 ]; do 
    echo "run main program, PID: $$" 
    sleep 3

    status=`ps -p $mon_pid -o pid| grep $mon_pid`
    if [ -z $status ]; then
        echo "main program finish"
        break
    fi
done
