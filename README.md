# CountDown App

Originally made as a countdown app strictly for my girlfriend's
vest date at the tech company she works at. She found that many
countdown application had an associated cost. I'm making this
one because I wanted to program and use my brain one day.

## Running the Application

1. Make sure you first install the xcode command line tools using:
```
$ xcode-select --install
```

2. Then install python-tk:
```
$ brew install python-tk
```

3. Simply open the terminal and run:
```
$ python run.py &
```

You'll have a countdown web-app just there. It'll update everyday.

**Note:** Make sure you are using python3

## Automating on OSX

Ideally this application should come up whenever you turn on the computer each day.

### Using Automator

Follow the provided guide from Apple to [Use a Shell Script Action in a Workflow](https://support.apple.com/guide/automator/use-a-shell-script-action-in-a-workflow-autbbd4cc11c/mac)

**Note:** Select Application as the type, add a call the `run.py` as seen
below, and save it in the applications folder.

The command to have automator run is:
```
$ ./<path-to-countdown>/run.sh
```

Now save the application with whatever name, you'd like. Now we can go ahead and add it to the startup:

1. Go to System Preferences
2. Go to Users and Groups
3. Click on Your Username
4. Click on Login Items
5. Click the plus sign
6. Select the application you Created

Now it'll launch at login!

### Cron

TODO

## Future of this Application

I will keep adding to this application to make it extensible
for anyone. I also want it to run on a web-server. 
No promises on when though.