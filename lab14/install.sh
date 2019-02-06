#!/bin/bash
if [[ -e /etc/Eos-release ]]
then
    echo -n "Found EOS - installing alias..."
    FastCli -c "en
                conf
                alias myrpm bash /opt/MyRPM/bin/MyRPM.sh "
    echo "done"
    echo -n "Saving Config..."
    FastCli -c "enable
                write"
    echo "done"
else
    echo 'Not EOS.'
fi
