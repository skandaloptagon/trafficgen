# TRAFFIC GEN

generate 15 seconds of packet generate on three servers back and forth accross all servers.

# Prefered setup

On each server:

* Open a `tmux` session. 
* `ctrl+b "` to split the window into two panes. 
* In one pane type `ITGRecv` to listen for incomming taffic.
* Switch panes using `ctrl+b down-arrow`
* `python server.py`

Now one one of your servers or on a seperate machine that can connect to your servers type `sh remote_gen.sh` to start generating traffic at the same time across all three servers.
