## Stucked with SSH?

If you can't SSH login due to some buggy profile files or bashrc commands you can try this method. Please read the original article [here](https://unix.stackexchange.com/questions/214042/cant-login-to-server-with-ssh-because-of-a-script-in-etc-profile-d-exiting-wit/480576#480576)

```
(trap '' INT; while true; do ssh myuser@myserver; done)
```

Then press and hold CTRL C, hopefully you will have a working `#bash` shell to fix bashrc or profile scripts.

_This is the only method which worked for me when I want to login without restarting services except sshd_
