## Your Cloud Backup & Sync Services { #cloud-backups }

All companies are advertising their use of end-to-end encryption (E2EE). This is true for almost every messaging app and website (HTTPS). Apple and Google are advertising their use of encryption on their Android devices and their iPhones.

But what about your backups? Those automated iCloud/Google Drive backups you have?

Well, you should know that most of those backups are not fully end-to-end encrypted and will hold some of your information readily available for a third party. You will see their claims that data is encrypted at rest and safe from anyone ... Except they usually do keep a key to access some of the data themselves. These keys are used for them indexing your content, recover your account, collecting various analytics.

There are specialized commercial forensics solutions available (Magnet Axiom[^248], Cellebrite Cloud[^249]) that will help an adversary analyze your cloud data with ease.

Notable Examples:

- Apple iCloud: <https://support.apple.com/en-us/HT202303> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-us/HT202303)</sup> : "Messages in iCloud also uses end-to-end encryption. If you have iCloud Backup turned on**, your backup includes a copy of the key protecting your Messages**. This ensures you can recover your Messages if you lose access to iCloud Keychain and your trusted devices. ".

- Google Drive and WhatsApp: <https://faq.whatsapp.com/android/chats/about-google-drive-backups/> <sup>[[Archive.org]](https://web.archive.org/web/https://faq.whatsapp.com/android/chats/about-google-drive-backups/)</sup>: "**Media and messages you back up aren't protected by WhatsApp end-to-end encryption while in Google Drive**. ". Do however note that Facebook/Whatsapp have announced the rollout of encrypted backups on October 14^th^ 2021 (<https://about.fb.com/news/2021/10/end-to-end-encrypted-backups-on-whatsapp/> <sup>[[Archive.org]](https://web.archive.org/web/https://about.fb.com/news/2021/10/end-to-end-encrypted-backups-on-whatsapp/)</sup>) which should solve this issue.

- Dropbox: <https://www.dropbox.com/privacy#terms> <sup>[[Archive.org]](https://web.archive.org/web/https://www.dropbox.com/privacy)</sup> "To provide these and other features, **Dropbox accesses, stores, and scans Your Stuff**. You give us permission to do those things, and this permission extends to our affiliates and trusted third parties we work with".

- Microsoft OneDrive: <https://privacy.microsoft.com/en-us/privacystatement> <sup>[[Archive.org]](https://web.archive.org/web/https://privacy.microsoft.com/en-us/privacystatement)</sup>: Productivity and communications products, "When you use OneDrive, we collect data about your usage of the service, as well as the content you store, to provide, improve, and protect the services. **Examples include indexing the contents of your OneDrive documents so that you can search for them later and using location information to enable you to search for photos based on where the photo was taken**".

You should not trust cloud providers with your (not previously and locally encrypted) sensitive data and you should be wary of their privacy claims. In most cases, they can access your data and provide it to a third party if they want to[^250].

The only way to mitigate this is to encrypt your data on your side and then only upload it to such services **or just not use them at all.**

