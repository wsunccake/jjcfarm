OPENMPI=/tmp/otter/openMPI

if [ -z "${PATH}" ]
then
  PATH=$OPENMPI/bin
else
  PATH=$OPENMPI/bin:$PATH
fi

if [ -z "${MANPATH}" ]
then
  MANPATH=$OPENMPI/share/man
else
  MANPATH=$OPENMPI/share/man:$MANPATH
fi

if [ -z "${LD_LIBRARY_PATH}" ]
then
  LD_LIBRARY_PATH=$OPENMPI/lib
else
  LD_LIBRARY_PATH=$OPENMPI/lib:$LD_LIBRARY_PATH
fi

if [ -z "${INCLUDE}" ]
then
  INCLUDE=$OPENMPI/include
else
  INCLUDE=$OPENMPI/include:$INCLUDE
fi

export PATH MANPATH LD_LIBRARY_PATH INCLUDE
