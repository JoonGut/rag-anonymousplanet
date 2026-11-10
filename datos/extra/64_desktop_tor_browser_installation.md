# Installing and Using Desktop Tor Browser { #desktop-tor-browser }

## Installation { #tor-browser-install }

This is valid for Windows, Linux, and macOS.

- Download and install Tor Browser according to the instructions from <https://www.torproject.org/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.torproject.org/download/)</sup>

- Open Tor Browser

## Usage and Precautions { #tor-browser-precautions }

- After opening Tor Browser, you will see an option to **Connect**, a checkbox to **Always connect automatically** and a button to **Configure connection**. The Tor Network settings are there for you to possibly configure Bridges to connect to Tor if you are experiencing issues connecting to Tor due to Censorship or Blocking. As explained here: [Using Tor bridges in hostile environments](#tor-bridges), this is now done automatically by the Tor Browser on Desktop.

![image55](../media/image55.png)

- Personally, in the case of censorship or blocking, we would recommend using Meek-Azure bridges if needed. And Snowflake bridges as a second option.

![image56](../media/image56.png)

At this point, still before connecting, you should click the little shield Icon (upper right, next to the Address bar) and select your Security level (see <https://tb-manual.torproject.org/security-settings/> <sup>[[Archive.org]](https://web.archive.org/web/https://tb-manual.torproject.org/security-settings/)</sup> for details). Basically, there are three.

![image57](../media/image57.png)

- Standard (the default):

    - All features are enabled (including JavaScript)

- Safer:

    - JavaScript is disabled on non-HTTPS websites

    - Some fonts and symbols are disabled

    - Any media playback is "click to play" (disabled by default)

- Safest:

    - Javascript is disabled everywhere

    - Some fonts and symbols are disabled

    - Any media playback is "click to play" (disabled by default)

We would recommend the "Safest" level by default. The "Safer" level should be enabled if you think you need access to a website not working without JavaScript. The Safest mode will  most likely break many websites that rely actively on JavaScript.

If you are extra paranoid, use the "Safest" level by default and consider downgrading to Safer is the website is unusable because of Javascript blocking.

**Optional and not recommended by the Tor Project**: If you are not using the "Safest" level, we will diverge from some but agree with others (for instance the Tails project and others[^525]) and will actually recommend some modifications of the default Tor Browser in the addition of two extensions:

- uBlock Origin (as it is the case on Tails) while leaving the extension on the default settings:

    - Head over to <https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/> within Tor Browser and install the extension.

- LibRedirect: This is very practical if you use the "Safest" mode as Invidious instances require no JavaScript.

    - Head over to <https://libredirect.github.io/> within Tor Browser and install the extension.

Let's keep in mind that even 3 letters agencies recommend blocking ads for their internal users in order to improve security[^526].

If you did not go for the above **personal and not officially recommended options**, the Safer level should still be used with some extra precautions while using some websites: see [Additional browser precautions with JavaScript enabled](#browser-precautions-js).

Now, you are really done, and you can now surf the web anonymously from your desktop device.

