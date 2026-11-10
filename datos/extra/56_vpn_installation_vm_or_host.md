# Installing a VPN on Your VM or Host OS { #vpn-installation }

Download the VPN client installer of your cash paid VPN service and install it on Host OS (Tor over VPN, VPN over Tor over VPN) or the VM of your choice (VPN over Tor):

- Whonix Tutorial (should work with any VPN provider): <https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor)</sup> (use the Linux configurations below to get the necessary configuration files)

- Windows Tutorials:

    - Mullvad: <https://mullvad.net/en/help/install-mullvad-app-windows/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/install-mullvad-app-windows/)</sup>

    - iVPN: <https://www.ivpn.net/apps-windows> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/apps-windows)</sup>

    - Safing: <https://docs.safing.io/portmaster/install/windows> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.safing.io/portmaster/install/windows)</sup>

    - Proton VPN: <https://protonvpn.com/support/protonvpn-windows-vpn-application/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/support/protonvpn-windows-vpn-application/)</sup>

- macOS:

    - Mullvad: <https://mullvad.net/en/help/install-and-use-mullvad-app-macos/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/install-and-use-mullvad-app-macos/)</sup>

    - IVPN: <https://www.ivpn.net/apps-macos/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/apps-macos/)</sup>

    - Safing: Not available on macOS

    - Proton VPN: <https://protonvpn.com/support/protonvpn-mac-vpn-application/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/support/protonvpn-mac-vpn-application/)</sup>

- Linux:

    - Mullvad: <https://mullvad.net/en/help/install-mullvad-app-linux/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/install-mullvad-app-linux/)</sup>

    - iVPN: <https://www.ivpn.net/apps-linux/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/apps-linux/)</sup>

    - Safing: <https://docs.safing.io/portmaster/install/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.safing.io/portmaster/install/linux)</sup>

    - Proton VPN: <https://protonvpn.com/support/linux-vpn-setup/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/support/linux-vpn-setup/)</sup>

**Important note: Tor does not support UDP, and you should use TCP instead with the VPN client in the Tor over VPN cases (on the VMs).**

In all cases, you should set the VPN to start from boot and enable the "kill switch" if you can. This is an extra step since this guide proposes solutions that all fall back on the Tor network in case of VPN failure.

Here are some guides provided by the recommended VPN providers in this guide:

- Windows:

    - iVPN: <https://www.ivpn.net/knowledgebase/general/do-you-offer-a-kill-switch-or-vpn-firewall/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/knowledgebase/general/do-you-offer-a-kill-switch-or-vpn-firewall/)</sup>

    - Proton VPN: <https://protonvpn.com/support/what-is-kill-switch/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/support/what-is-kill-switch/)</sup>

    - Mullvad: <https://mullvad.net/en/help/using-mullvad-vpn-app/#killswitch> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/using-mullvad-vpn-app/)</sup>

- Whonix Workstation: Coming Soon, it is certainly possible, but we did not find a suitable and easy tutorial yet. It is also worth remembering that if your VPN stops on Whonix, you will still be behind the Tor Network.

- macOS:

    - Mullvad same as Windows, the option should be in the provided VPN client

    - iVPN same as Windows, the option should be in the provided VPN client

    - Proton VPN same as Windows with the client, the option should be in the provided VPN client <https://protonvpn.com/blog/macos-vpn-kill-switch/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/blog/macos-vpn-kill-switch/)</sup>

- Linux:

    - Mullvad:

        + <https://mullvad.net/en/help/wireguard-and-mullvad-vpn/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/wireguard-and-mullvad-vpn/)</sup>

        + <https://mullvad.net/en/help/linux-openvpn-installation/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/linux-openvpn-installation/)</sup>

    - Proton VPN: <https://github.com/ProtonVPN/linux-cli/blob/master/USAGE.md#kill-switch> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/ProtonVPN/linux-cli/blob/master/USAGE.md)</sup>

    - iVPN:

        + <https://www.ivpn.net/knowledgebase/linux/linux-wireguard-kill-switch/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/knowledgebase/linux/linux-wireguard-kill-switch/)</sup>

        + <https://www.ivpn.net/knowledgebase/linux/linux-kill-switch-using-the-uncomplicated-firewall-ufw/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/knowledgebase/linux/linux-kill-switch-using-the-uncomplicated-firewall-ufw/)</sup>

