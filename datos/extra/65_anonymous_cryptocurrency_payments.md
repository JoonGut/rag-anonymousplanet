# Anonymous Cryptocurrency Payments { #anonymous-crypto-payments }

There are many services that you might want to use (VPS hosting, mail hosting, domain names...) but require payment of some kind.

As mentioned before in this guide multiple times, we strongly recommend the use of services accepting cash (that you could send anonymously through the postal services) or Monero which you can buy and use directly and safely.

- But what if the service you want does not accept Monero but does accept a more mainstream cryptocurrency such as Bitcoin (BTC) or Ethereum (ETH)?

**Bitcoin and other "mainstream cryptocurrencies" are not anonymous at all (Remember [Your Crypto Transactions](#crypto-transactions)) and you should never ever purchase, for example, Bitcoin from an exchange and then use these directly for purchasing services anonymously. This will not work, and the transaction can be traced easily.**

- **Stay away from so-called "private" mixers, tumblers and coinjoiners.** You might think this is a good idea, but not only are they useless with cryptocurrencies such as BTC/ETH/LTC, they are also dangerous. They take custody of your coins. Use Monero to anonymize your crypto. Do not use a normal KYC-enabled exchange to buy/sell your Monero (such as Kraken), since this information on your purchases and withdrawals (for intended use) are retained in the exchange. Instead, use a P2P exchange that doesn't require KYC such as what can be found on <https://kycnot.me/>.

- **See [Warning about special tumbling, mixing, coinjoining privacy wallets and services](#on-tumbling).**

## Using Bitcoin anonymously option { #use-bitcoin-anonymously }

Despite this, it is possible to safely anonymize Bitcoin through the use of non-custodial collaborative transactions and privacy-preserving spending tools. This is possible with a protocol called [ZeroLink](https://code.samourai.io/whirlpool/Whirlpool/-/blob/whirlpool/THEORY.md) and an implementation called Whirlpool which as two clients that utilize it and provide the necessary spending tools, detailed below. So, you might be wondering how? Well, it is actually pretty simple:

1. Purchase Bitcoin at a non-KYC exchange (such as one found on <https://kycnot.me/>)

2. Create a wallet with [Samourai Wallet](https://www.samouraiwallet.com/) (Android) or [Sparrow Wallet](https://www.sparrowwallet.com/) (Desktop). Both of these use the Whirlpool protocol to gain the user forward-facing on-chain privacy on Bitcoin.

3. Deposit coins into the wallet and follow the relevant instructions ([Samourai](https://docs.samourai.io/wallet/usage), [Sparrow](https://www.sparrowwallet.com/docs/mixing-whirlpool.html)) to remove their historic links.

4. Funds should only be spent from the Postmix account, as that is the account with the coins that have gained anonymity through Whirlpool.

- **You should run your own node when using Bitcoin and always use that for connecting from your wallet. You do not need to purchase separate hardware to do so, and it's simple to [do so by using the Tor Network](https://bitcoincoredocs.com/tor.html) as well.**

## Using Monero anonymously option { #use-monero-anonymously }

1. Purchase Monero at a non-KYC exchange (such as one found on <https://kycnot.me/>)

2. Create a Monero wallet on one of your anonymized VMs (for example, on the Whonix Workstation which includes a Monero GUI wallet natively or using the Monero GUI wallet from <https://www.getmonero.org/downloads/> on other OSes)

3. Transfer your Monero from the wallet from which you bought it to the wallet on your VM. We cannot stress enough how import it is to have two separate wallets for this process, even for handling Monero.

4. On the same VM (for instance again the Whonix Workstation), create a Bitcoin Wallet (again this is provided natively within the Whonix Workstation)

5. From an anonymized browser (such as Tor Browser), use a non-KYC (Know Your Customer) service swapping service (see [Crypto Swapping Services without Registration and KYC](#crypto-swapping-no-kyc)) and convert your Monero to BTC and transfer those to the BTC Wallet you have on your anonymized VM

6. You should now have an anonymized Bitcoin wallet that can be used for purchasing services that do not accept Monero.

**You should never access this wallet from a non-anonymized environment. Always use well-thought OPSEC with your BTC transactions. Remember those can be traced back to you.**

The origin of those BTC cannot be traced back to your real identity due to the use of Monero **unless Monero is broken** or if you consolidate outputs from spending at separate merchants. It is recommended to use privacy preserving wallets in the [Bitcoin section](#use-bitcoin-anonymously). Please do read [Monero Disclaimer](#monero-disclaimer).

**Regarding Zcash: this section previously included use of Zcash but it has been removed in light of newer, more accurate information.**

## Warning about special tumbling, mixing, coinjoining privacy wallets and services { #on-tumbling }

Centralized "private" tumblers, mixers and coinjoiners are not recommended since they do not provide anonymity in a way that truly unlinks an output from its history.  Here are some references about this issue:

- [Mixing detection on Bitcoin transactions using statistical patterns.](https://arxiv.org/pdf/2204.02019.pdf) <sup>[Archive.org](https://web.archive.org/web/https://arxiv.org/pdf/2204.02019.pdf)</sup>
- [An Analysis Of Bitcoin Laundry Services](https://www.researchgate.net/profile/Julio-Hernandez-Castro/publication/319944399_An_Analysis_of_Bitcoin_Laundry_Services/links/5a045d410f7e9beb177883af/An-Analysis-of-Bitcoin-Laundry-Services.pdf?origin=publication_detail) <sup>[Archive.org](https://web.archive.org/web/https://www.researchgate.net/profile/Julio-Hernandez-Castro/publication/319944399_An_Analysis_of_Bitcoin_Laundry_Services/links/5a045d410f7e9beb177883af/An-Analysis-of-Bitcoin-Laundry-Services.pdf?origin=publication_detail)</sup>
- [Mixing Strategies in Cryptocurrencies and An Alternative Implementation](https://www.researchgate.net/publication/344485520_Mixing_Strategies_in_Cryptocurrencies_and_An_Alternative_Implementation) <sup>[Archive.org](https://web.archive.org/web/https://www.researchgate.net/publication/344485520_Mixing_Strategies_in_Cryptocurrencies_and_An_Alternative_Implementation)</sup>

Mixing BTC in this way should prevent any chain analysis on future transactions. This will _not_ however hide any past transactions or the fact you purchased BTC from a KYC exchange. Instead we recommend to use Bitcoin wallets that utilize Whirlpool or Monero (preferred).

## When converting from BTC to Monero { #atomic-swap-xmr }

**Now, as part of any process above, if you want to convert BTC back to Monero**, we recommend not using a swapping service but instead recommend using the new Monero Atomic Swap Tool: <https://unstoppableswap.net/>. This will prevent unnecessary fees and intermediates when using a commercial swapping service. The website is self-explanatory with detailed instructions for all OSes.

