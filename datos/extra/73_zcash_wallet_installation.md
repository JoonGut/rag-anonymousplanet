# Installing a Zcash Wallet { #zcash-wallet }

Remember this should only be done on a secure environment such as VM behind the Whonix Gateway.

## Debian 11 VM { #zcash-debian }

- Load the Debian VM

- Open a browser

- Go to <https://packages.debian.org/buster/amd64/libindicator3-7/download> and download from a listed mirror.

- Go to <https://packages.debian.org/buster/amd64/libappindicator3-1/download> and download from a listed mirror.

- Go to the ZecWallet Lite Website to download the latest DEB package <https://www.zecwallet.co/#download> (change the download directory to /home/user for convenience)

- Open a Terminal window and run the following commands (with the updated downloaded version if needed):

    - ```sudo dpkg -i ./libindicator3-7_0.5.0-4_amd64.deb```

    - ```sudo dpkg -i ./libappindicator3-1_0.4.92-7_amd64.deb```

    - ```sudo dpkg -i ./Zecwallet_Lite_1.7.5_amd64.deb```

- Click the upper left menu, find then launch ZecWallet Lite

## Ubuntu 20.04/21.04/21.10 VM { #zcash-ubuntu }

- Load the Ubuntu VM

- Open a browser

- Go to the ZecWallet Lite Website to download the latest DEB package <https://www.zecwallet.co/#download>

- Open a Terminal window

- Go to your download directory and run the following command (with the updated downloaded version if needed), for example: ```sudo apt install ./Zecwallet_Lite_1.7.5_amd64.deb```

- Click the upper left menu, find then launch ZecWallet Lite

## Windows 10/11 VM { #zcash-windows }

- Load the Windows VM

- Open a browser

- Go to <https://www.zecwallet.co/#download>

- Download and install the latest Windows installer

- Launch ZecWallet Lite

## Whonix Workstation 16 VM { #zcash-whonix }

- Load the Whonix Workstation VM

- Open Tor Browser

- Go to <https://packages.debian.org/buster/amd64/libindicator3-7/download> and download from a listed mirror.

- Go to <https://packages.debian.org/buster/amd64/libappindicator3-1/download> and download from a listed mirror.

- Go to the ZecWallet Lite Website to download the latest DEB package <https://www.zecwallet.co/#download> (change the download directory to /home/user for convenience)

- Open a Terminal window and run the following commands (with the updated downloaded version if needed):

    - ```sudo dpkg -i ./libindicator3-7_0.5.0-4_amd64.deb```

    - ```sudo dpkg -i ./libappindicator3-1_0.4.92-7_amd64.deb```

    - ```sudo dpkg -i ./Zecwallet_Lite_1.7.5_amd64.deb```

- Click the upper left menu and go to Development, then launch ZecWallet Lite

