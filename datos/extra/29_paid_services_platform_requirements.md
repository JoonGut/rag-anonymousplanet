### About paid services { #paid-services }

If you intend to use paid services, privilege those accepting cash payments or Monero payments which you can do directly and safely while keeping your anonymity.

If the service you intend to buy does not accept those but accepts Bitcoin (BTC), consider the following appendix: [Paying anonymously online with BTC (or any other cryptocurrency)](#anonymous-crypto-payments).

This section will show you an overview of the current various requirements on some platforms:

- **Consider using the recommended tools on <https://privacyguides.org>** <sup>[[Archive.org]](https://web.archive.org/web/https://privacyguides.org)</sup> **for better privacy instead of the usual mainstream ones.**

- **Consider using the recommended tools on <https://www.whonix.org/wiki/Documentation>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Documentation)</sup> **as well instead of the usual mainstream ones such as E-mail providers: <https://www.whonix.org/wiki/E-Mail#Anonymity_Friendly_Email_Provider_List>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/E-Mail#Anonymity_Friendly_Email_Provider_List)</sup>

**The following overview does not mention the privacy practices of those platforms but only their requirements for registering an account. If you want to use privacy-aware tools and platforms, head on to <https://privacyguides.org>** <sup>[[Archive.org]](https://web.archive.org/web/https://privacyguides.org/)</sup>**.**

Legend:

- "Unclear": Unclear due to lack of information or confusing information.

- "Maybe": It did happen in a minority of my tests.

- "Likely": It did happen in most of my tests.

- "Yes" or "No": This either happened or never happened systematically in all my tests.

- "Easy": The overall experience was straightforward with little to no obstacles.

- "Medium": The overall experience has some obstacles, but it is still doable without too much hassle.

- "Hard": The overall experience is a painful struggle with many obstacles.

- "N/A": Not Applicable because it was not possible to test within the context of this guide

- "Indirectly": This means they do require something but indirectly through a third-party system (Financial KYC for example).

- **See [The Real-Name System](#real-name-system) for essential information. See below for details.**

**Below you'll find a list of "problematic services". If they're not below, it means there are no issues at all with anything (like Briar for example)**

**Amazon**

- Is this against their ToS? No, but yes <https://www.amazon.com/gp/help/customer/display.html?nodeId=202140280> <sup>[[Archive.org]](https://web.archive.org/web/https://www.amazon.com/gp/help/customer/display.html?nodeId=202140280)</sup>

"1. Amazon Services, Amazon Software

A. Use of Amazon Services on a Product. To use certain Amazon Services on a Product, you must have your own Amazon.com account, be logged in to your account on the Product, **and have a valid payment method associated with your account.** "

While it does not technically require a real name. It does require a valid payment method. Unfortunately, it will not accept "cash" or "Monero" as a payment method. So instead, they are relying on financial KYC (where a real-name policy is pretty much enforced everywhere).

- Will they require a phone number? Yes, but see below

- Can you create accounts through Tor? Yes, but see below

Because of this valid payment method requirement, we could not test this. While this is seemingly not against their ToS, it is not possible within the context of this guide unless you manage to obtain a valid KYC payment method anonymously which AFAIK is pretty much impossible or extremely difficult.

So, AFAIK, it is not possible to create an anonymous Amazon account.

**Apple**

- Is this against their ToS? Yes <https://www.apple.com/legal/internet-services/icloud/en/terms.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.apple.com/legal/internet-services/icloud/en/terms.html)</sup>

"IV. Your Use of the Service

A. Your Account

In order to use the Service, you must enter your Apple ID and password to authenticate your Account**. You agree to provide accurate and complete information when you register with, and as you use, the Service ("Service Registration Data"), and you agree to update your Service Registration Data to keep it accurate and complete".**

- Will they require a phone number? Yes

- Can you create accounts through Tor? Yes

Note that this account will not allow you to set up an Apple mail account. For that, you will need an Apple device.

**Binance**

- Is this against their ToS? Yes <https://www.binance.com/en/terms> <sup>[[Archive.org]](https://web.archive.org/web/https://www.binance.com/en/terms)</sup>

- Will they require a phone number? No, they do require an e-mail

- Can you create accounts through Tor? No

**Discord**

- Is this against their ToS? No <https://discord.com/terms> <sup>[[Archive.org]](https://web.archive.org/web/https://discord.com/terms)</sup>

- Will they require a phone number? No, but they do require an e-mail

- Can you create accounts through Tor? We had no issues with that so far using the Desktop Client

You might encounter more issues using the Web Client (Captchas). Especially with Tor Browser.

I suggest using the Discord Client app on a VM through Tor or ideally through VPN/Proxy over Tor to mitigate such issues.

**Element**

- Is this against their ToS? No <https://element.io/terms-of-service> <sup>[[Archive.org]](https://web.archive.org/web/https://element.io/terms-of-service)</sup>

- Will they require a phone number? No, they do not even require an e-mail

- Can you create accounts through Tor? Yes

Expect some Captchas during account creation on some homeservers.

**Facebook**

- Is this against their ToS? Yes <https://www.facebook.com/terms.php> <sup>[[Archive.org]](https://web.archive.org/web/https://www.facebook.com/terms.php)</sup>

"1. Who can use Facebook

When people stand behind their opinions and actions, our community is safer and more accountable. For this reason, you must:

- Use the same name that you use in everyday life.

- Provide accurate information about yourself.

- Will they require a phone number? Yes, and probably more later

- Can you create accounts through Tor? Yes, but it is very difficult and their onion address[^398] will not help. In most cases, you'll just have a random error at sign-up and your account suspended after sign-in."

But this clause of their ToS is illegal in Germany (see [Requirements](#requirements-limitations)).

Facebook is one of the most aggressive platforms with identity verification and is pushing hard their "real name policy". It is why this guide is only advised to German residents.

Over our tests tho we were able to pinpoint a few tips:

- It will be easier if you have an Instagram account first.

- Signing up through Tor is almost impossible (even using their .onion address which is a joke) and will only succeed if you are " very lucky" (I assume if you are using an exit node that is not yet known by Facebook verification systems). In most cases, it will not allow registration at all and will just fail with "An error has occurred during registration".

- Signing up through VPNs is more likely to succeed but might still result in the same error. So, you must be ready for a lot of trial and error here.

- Signing up through a Self-Hosted VPN/Proxy is your best bet but make sure your profile/identity matches the IP geolocation.

- My earlier entry in the guide about the Orwellian quote from Animal Farm is in full effect on Facebook. You will experience huge variation in acceptance depending on age/sex/ethnicity/nationality/... This is where you will have far fewer issues if you are making an account of a Young European Caucasian Female. You will almost certainly fail if you try making a Middle-Aged Male where my other accounts are still unsuspended/unbanned to this day.

- Logging-in (after you sign-up) however works fine with VPN and Tor but might still trigger an account suspension for violating Community Guidelines or Terms of Services (despite you not using the account at all for anything else than signing-up/logging-in). Ideally, you should log-in back with the same IP from a self-hosted VPN/Proxy.

I also suspect strongly based on my test that the following points have an impact on your likelihood of being suspended over time:

- Not having friends

- Not having interests and an "organic activity"

- Not being in the contacts of any other user

- Not being on other platforms (such as Instagram/WhatsApp)

- Restricting your profile privacy settings too soon after signing-up

If your account gets suspended, you will need to appeal the decision through a quite simple form that will require you to submit a "proof of ID". However, that proof of ID verification system is more lenient than LinkedIn and will allow you to send various documents which require far less Photoshop skills.

It is also possible that they ask you to take a selfie video or picture-making certain gestures to prove your identity. If that is the case, we are afraid it is a dead-end for now unless you use a deepfake face swapping technique.

If you do file an appeal, you will have to wait for Facebook to review it (I do not know whether this is automatic or human) and you will have to wait and hope for them to unsuspend your account.

**GitHub**

- Is this against their ToS? No <https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-terms-of-service> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-terms-of-service)</sup>

- Will they require a phone number? Nope, all good

- Can you create accounts through Tor? Yes, but expect some captchas

GitHub is straightforward and requires no phone number.

Be sure to go into Settings > E-Mail and make your e-mail private as well as block any push that would reveal your e-mail.

**GitLab**

- Is this against their ToS? No <https://about.gitlab.com/handbook/legal/subscription-agreement/> <sup>[[Archive.org]](https://web.archive.org/web/https://about.gitlab.com/handbook/legal/subscription-agreement/)</sup>

- Will they require a phone number? Nope, all good

- Can you create accounts through Tor? Yes, but expect captchas

GitLab is straightforward and requires no phone number.

**Google**

- Is this against their ToS? No <https://policies.google.com/terms> <sup>[[Archive.org]](https://web.archive.org/web/https://policies.google.com/terms)</sup>

- Will they require a phone number? Yes, they will. There is no escape here.

- Can you create accounts through Tor? Yes, but expect some captchas and your phone number will be required

Proton is good ... but to appear less suspicious, it is simply better to also have a mainstream Google Mail account.

As Proton, Google will also most likely require a phone number during sign-up as part of their verification process. However contrary to Proton, Google will store that phone number during the sign-up process and will also limit the number of accounts that can be created during the sign-up[^399]'[^400].

From my experience during my research, this count is limited to three accounts/phone numbers. If you are unlucky with your number (if it was previously used by another mobile user), it might be less.

You should therefore use again your online phone number OR your burner phone and pre-paid SIM card to create the account. Do not forget to use the identity details you made up earlier (birthdate). When the account is created, please do take some time to do the following:

- **(Trick)** Log into Google Mail on desktop and go into the Gmail Quick Settings > See all Setting > Forwarding and POP/IMAP > Add a forwarding address > Verify (using Proton) > Go back to Gmail and set the forwarding to forward and delete Google copy > Save. This step will allow you to check your Google Mail using Proton instead and will allow you to avoid triggering Google Security checks by Logging in from various VPN/Tor exit IP addresses in the future while storing your sensitive e-mail at Proton instead. This trick will allow you to receive all the e-mails from your Gmail addresses on your Proton (or other) address without needing to login into your Google accounts (reducing risks of it being suspended, especially if you use Tor).

- Enable 2FA within the Google account settings. First, you will have to enable 2FA using the phone number. Then you will see the option appear to enable 2FA using an Authenticator app. Use that option and set it up with a new KeePassXC TOTP entry. When it is done, remove the phone 2FA from the Google account. This will prevent someone from using that phone number in the future (when you do not have it anymore) to recover/gain access to that account.

- Add Proton as a recovery e-mail address for the account.

- Remove the phone number from the account details as a recovery option.

- Upload a Google profile picture you made earlier during the identity creation step.

- Review the Google Privacy settings to disable as much as you can:

    - Activity logging

    - YouTube

- Log out and do not touch it unless needed (as mentioned, you will use Proton to check your Gmail).

Keep in mind that there are different algorithms in place to check for weird activity. If you receive any mail (on Proton) prompting about a Google Security Warning. Click it and click the button to say, "Yes it was me". It helps.

Do not use that account for "sign-up with Google" anywhere unless necessary.

Be extremely careful if you decide to use the account for Google activities (such as Google Maps reviews or YouTube Comments) as those can easily trigger some checks (Negative reviews, Comments breaking Community Guidelines on YouTube).

If your account gets suspended [^401] (this can happen on sign-up, after signing-up or after using it in some Google services), you can still get it unsuspended by submitting[^402] an appeal/verification (which will again require your Phone number and possibly an e-mail contact with Google support with the reason). **Suspension of the account does not disable the e-mail forwarding, but the suspended account will be deleted after a while.**

After suspension, if your Google account is restored, you should be fine.

If your account gets banned, you will have no appeal and the forwarding will be disabled. Your phone number will be flagged, and you will not be able to use it to sign-up on a different account. Be careful when using those to avoid losing them. They are precious.

It is also possible that Google will require an ID check through indirect financial KYC or ID picture check if you try to access/publish mature content on their platform[^403].

**Instagram**

- Is this against their ToS? **Maybe?** We are not sure <https://help.instagram.com/581066165581870?ref=dp> <sup>[[Archive.org]](https://web.archive.org/web/https://help.instagram.com/581066165581870?ref=dp)</sup>

"**You can't impersonate others or provide inaccurate information. You do not have to disclose your identity on Instagram, but you must provide us with accurate and up-to-date information (including registration information)**. **Also, you may not impersonate someone you are not, and you can't create an account for someone else unless you have their express permission".**

This one is a bit of an Oxymoron don't you think? So, we are not sure whether it is allowed or not.

- Will they require a phone number? Maybe but less likely over VPN and very likely over Tor

- Can you create accounts through Tor? Yes, but expect some captchas and your phone number will be required

It is also possible that they ask you to take a selfie video or picture-making certain gestures to prove your identity (within the app or through an e-mail request). If that is the case, we are afraid it is a dead-end for now.

It is no secret that Instagram is part of Facebook however it is more lenient than Facebook when it comes to user verification. It is quite unlikely you will get suspended or banned after signing up. But it could help.

For instance, we noticed that you will face fewer issues creating a Facebook account if you already have a valid Instagram account. You should always create an Instagram account before trying Facebook.

Unfortunately, there are some limitations when using the web version of Instagram. For instance, you will not be able to enable Authenticator 2FA from the web for a reason we do not know.

After sign-up, do the following:

- Upload a picture of your generated identity if you want.

- Go into your Settings

- Make the account private (initially at least)

- Do not show activity status

- Do not allow sharing

**Jami**

- Is this against their ToS? No <https://jami.net/privacy-policy/> <sup>[[Archive.org]](https://web.archive.org/web/https://jami.net/privacy-policy/)</sup>

- Will they require a phone number? No, they do not even require an e-mail

- Can you create accounts through Tor? Nope it does not work for some technical reason

**Kraken**

- Is this against their ToS? Yes <https://www.kraken.com/legal> <sup>[[Archive.org]](https://web.archive.org/web/https://www.kraken.com/legal)</sup>

- Will they require a phone number? No, they do require an e-mail

- Can you create accounts through Tor? Yes

**LinkedIn**

- Is this against their ToS? Yes <https://www.linkedin.com/legal/user-agreement> <sup>[[Archive.org]](https://web.archive.org/web/https://www.linkedin.com/legal/user-agreement)</sup>

"To use the Services, you agree that: (1) you must be the "_Minimum Age_" (described below) or older; (2) **you will only have one LinkedIn account, which must be in your real name**; and (3) you are not already restricted by LinkedIn from using the Services. **Creating an account with false information is a violation of our terms**, including accounts registered on behalf of others or persons under the age of sixteen. "

But this clause of their ToS is illegal in Germany (see [Requirements](#requirements-limitations)).

- Will they require a phone number? Yes, they will.

- Can you create accounts through Tor? Yes, but expect some captchas and your phone number will be required

LinkedIn is far less aggressive than twitter but will nonetheless require a valid e-mail (preferably again your Gmail) and a phone number in most cases (tho not always).

LinkedIn however is relying a lot on reports and user/customer moderation. You should not create a profile with an occupation inside a private corporation or a small startup company. The company employees are monitoring LinkedIn activity and receive notifications when new people join. They can then report your profile as fake, and your profile will then be suspended or banned pending appeal.

LinkedIn will then require you to go through a verification process that will, unfortunately, require you to send an ID proof (identity card, passport, driver's license). This ID verification is processed by a company called Jumio[^404] that specializes in ID proofing. This is most likely a dead end as this would force you to develop some strong Photoshop skills.

Instead, you are far less likely to be reported if you just stay vague (say you are a student/intern/freelance) or pretend you work for a large public institution that is too large for anyone to care or check.

As with Twitter and Google, you should do the following after signing up:

- Disable ads

- Disable notifications

- Disable lookup by phone/e-mail

- Upload a picture of your identity

**MailFence**

- Is this against their ToS? No

- Will they require a phone number? No, but they require an e-mail

- Can you create accounts through Tor? Maybe. From my tests, the signing-up verification e-mails are not sent when using Tor to sign-up. No issues however when using a VPN over Tor or a Proxy over Tor.

**Medium**

- Is this against their ToS? No, unless it is about crypto <https://policy.medium.com/medium-terms-of-service-9db0094a1e0f> <sup>[[Archive.org]](https://web.archive.org/web/https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)</sup>

- Will they require a phone number? No, but they require an e-mail

- Can you create accounts through Tor? No issues with that so far

Signing-in does require an e-mail every time.

**Microsoft**

- Is this against their ToS? Yes <https://www.microsoft.com/en/servicesagreement/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.microsoft.com/en/servicesagreement/)</sup>

"i. Creating an Account. You can create a Microsoft account by signing up online. **You agree not to use any false, inaccurate, or misleading information when signing up for your Microsoft account".**

But this clause of their ToS is illegal in Germany (see [Requirements](#requirements-limitations)).

- Will they require a phone number? Likely but not always. Depending on your luck with your Tor exit node, they may only require e-mail verification. If you use a VPN over Tor, they will likely only ask for an e-mail.

- Can you create accounts through Tor? Yes, you can but expect captchas, at least e-mail verification, **and likely phone verification.**

So yes, it is still possible to create an MS account without a phone number and using Tor or VPN, but you might have to cycle through a few exit nodes to achieve this.

After signing up you should set up 2FA authentication within the security options and using KeePassXC TOTP.

**OnlyFans**

- Is this against their ToS? No, it looks fine <https://onlyfans.com/terms> <sup>[[Archive.org]](https://web.archive.org/web/https://onlyfans.com/terms)</sup>

- Will they require a phone number? No, they do require an e-mail

- Can you create accounts through Tor? Yes, you can

Unfortunately, you will be extremely limited with that account and to do anything you will need dot complete their verification process which requires a KYC type financial transaction check. So, not very useful.

**Proton**

- Is this against their ToS? No <https://proton.me/legal/terms> <sup>[[Archive.org]](https://web.archive.org/web/https://proton.me/legal/terms)</sup>

- Will they require a phone number? Maybe. This depends on the IP you are coming from. If you come from Tor, it is likely. From a VPN, it is less likely.

- Can you create accounts through Tor? Yes, but highly likely that a phone number will be required when only an e-mail or a captcha will be required over a VPN. They even have a ".onion" address at <http://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/>.

You obviously need an e-mail for your online identity and disposable e-mails are pretty much banned everywhere.

Proton is a free e-mail provider based in Switzerland that advocates security and privacy.

They are recommended by Privacyguides.org[^405]. Their only apparent issue is that they do require (in most cases) a phone number or another e-mail address for registration (when you try to register from a VPN or Tor at least).

They claim they do not store/link the phone/e-mail associated with the registration but only store a hash that is not linked to the account[^406]. If their claim is true and the hash is not linked to your account, and that you followed my guide about the phone number, you should be reasonably safe from tracking.

This e-mail account can be used for creating a Google/Gmail account.

**Reddit**

- Is this against their ToS? No <https://www.redditinc.com/policies> <sup>[[Archive.org]](https://web.archive.org/web/https://www.redditinc.com/policies)</sup>

- Will they require a phone number? No, they will not.

- Can you create accounts through Tor? Yes

Reddit is simple. All you need to register is a valid username and a password. Normally they do not even require an e-mail (you can skip the e-mail when registering, leaving it blank).

No issues whatsoever signing up over Tor or VPN besides the occasional Captchas.

Consider reading this reddit post: <https://old.reddit.com/r/ShadowBan/comments/8a2gpk/an_unofficial_guide_on_how_to_avoid_being/> <sup>[[Archive.org]](https://web.archive.org/web/https://old.reddit.com/r/ShadowBan/comments/8a2gpk/an_unofficial_guide_on_how_to_avoid_being/)</sup>

**Slashdot**

- Is this against their ToS? Yes <https://slashdotmedia.com/terms-of-use/> <sup>[[Archive.org]](https://web.archive.org/web/https://slashdotmedia.com/terms-of-use/)</sup>

"8. Registration; Use of Secure Areas and Passwords

Some areas of the Sites may require you to register with us. When and if you register, you agree to (a) provide accurate, current, and complete information about yourself as prompted by our registration form (including your e-mail address) and (b) to maintain and update your information (including your e-mail address) to keep it accurate, current, and complete. You acknowledge that should any information provided by you be found to be untrue, inaccurate, not current, or incomplete, we reserve the right to terminate this Agreement with you and your current or future use of the Sites (or any portion thereof)".

- Will they require a phone number? No

- Can you create accounts through Tor? Yes

**Telegram**

- Is this against their ToS? No <https://telegram.org/tos> <sup>[[Archive.org]](https://web.archive.org/web/https://telegram.org/tos)</sup>

- Will they require a phone number? Yes unfortunately

- Can you create accounts through Tor? Yes, but sometimes you randomly get banned without any reason

Telegram is quite straightforward, and you can download their portable Windows app to sign-up and log in.

It will require a phone number (that can only be used once) and nothing else.

In most cases, we had no issues whether it was over Tor or VPN, but we had a few cases where our telegram account was just banned for violating terms of services (not sure which one?). This again despite not using them for anything.

They provide an appeal process through e-mail, but we had no success with getting any answer.

Their appeal process is just sending an e-mail to <recover@telegram.org> <sup>[[Archive.org]](https://web.archive.org/web/mailto:recover@telegram.org)</sup> stating your phone number and issue and hope they answer.

After signing up you should do the following:

- Go into Edit profile

- Set a Username

- Go into Settings (Desktop App)

- Set the Phone Number visibility to Nobody

- Set Last Seen & Online to Nobody

- Set Forwarded Messages to Nobody

- Set Profile photos to Contacts

- Set Calls to Contacts

- Set Group & Channels to Contacts

**Tutanota**

- Is this against their ToS? No <https://tutanota.com/terms/> <sup>[[Archive.org]](https://web.archive.org/web/https://tutanota.com/terms/)</sup>

- Will they require a phone number? No, but they do require an e-mail.

- Can you create accounts through Tor? Not really, almost all Tor Exit nodes are banned AFAIK

**Twitter**

- Is this against their ToS? No <https://twitter.com/en/tos>

- Will they require a phone number? Extremely likely, possibly now a requirement in all cases.

- Can you create accounts through Tor? Yes, but expect some captchas and your phone number will be required after a while.

Twitter is extremely aggressive in preventing anonymity on its network. You should sign-up using e-mail and password (not phone) and not using "Sign-in with Google". Use your Gmail as the e-mail address.

More than likely, your account will be suspended immediately during the sign-up process and will require you to complete a series of automated tests to unlock. This will include a series of captchas, confirmation of your e-mail and Twitter handle, or other information. In some cases, it will also require your phone number.

In some cases, despite you selecting a text verification, the Twitter verification system will call the phone no matter what. In that case, you will have to pick up and hear the verification code. We suspect this is another method of preventing automated systems and malicious companies or entities from selling text receiving services over the internet.

Twitter will store all this information and link it to your account including your IP, e-mail, and phone number. You will not be able that phone number to create a different account.

Once the account is restored, you should take some time to do the following:

- Upload the identity profile picture.

- Enable 2FA from the security settings using a new KeePassXC TOTP entry, save the security codes in KeePassXC as well.

- Disable Photo tagging

- Disable E-mail lookup

- Disable Phone lookup

- Disable all personalized advertising settings

- Disable geolocation of tweets

- **Caution:** Remove the phone number from the account (at your own risk, this often leads to suspension of the account)

- Follow some people based

- Log out and leave it be.

After about a week, you should check Twitter again and the chances are quite high that it will be suspended again for "suspicious activity" or "violating community guidelines" despite you not using it at all (not even a single tweet/follow/like/retweet or DM) but this time by another system. We call this the "Double-tap".

This time you will need to submit an appeal using a form[^407], provide a good reason and wait for the appeal to be processed by Twitter. During that process, you may receive an e-mail (on Proton) asking you to reply to a customer service ticket to prove that you do have access to your e-mail and that it is you. This will be directed toward your Gmail address but will arrive on your Proton.

Do not reply from Proton as this will raise suspicions, you must sign in to Gmail (unfortunately) and compose a new mail from there copy-pasting the E-Mail, Subject, and Content from Proton. As well as a reply confirming you have access to that e-mail.

After a few days, your account should get unsuspended "for good". No issues after that but keep in mind they can still ban your account for any reason if you violate the community guidelines. The phone number and e-mail will then be flagged, and you will have no other option but to get a new identity with a new number to sign-up again. Do not use this account for trolling.

**Twitch**

- Is this against their ToS? No <https://www.twitch.tv/p/en/legal/terms-of-service/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.twitch.tv/p/en/legal/terms-of-service/)</sup>

- Will they require a phone number? No, but they do require an e-mail.

- Can you create accounts through Tor? Yes

Note that you will not be able to enable 2FA on Twitch using only e-mail. This feature requires a phone number to enable.

**WhatsApp**

- Is this against their ToS? **Yes** <https://www.whatsapp.com/legal/updates/terms-of-service-eea> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whatsapp.com/legal/updates/terms-of-service-eea)</sup>

"**Registration**. You must register for our Services **using accurate information**, provide your current mobile phone number, and, if you change it, update your mobile phone number using our in-app change number feature. You agree to receive text messages and phone calls (from us or our third-party providers) with codes to register for our Services".

- Will they require a phone number? Yes, they do.

- Can you create accounts through Tor? No issues with that so far.

**4chan**

- Is this against their ToS? No

- Will they require a phone number? No, they will not.

- Can you post there with Tor or VPN? Not likely.

4chan is 4chan ... This guide will not explain 4chan to you. They block Tor exit nodes and known VPN IP ranges.

You are going to have to find a separate way to post there using at least seven proxies[^408] that are not known by 4chan blocking system (hint: Anonymous VPS using Monero is probably your best option).

![image40](../media/image40.png)

**Crypto Wallets**

Use any crypto wallet app within the Windows Virtual Machine. But be careful not to transfer anything toward an Exchange or a known Wallet. Crypto is in most cases NOT anonymous and can be traced back to you when you buy/sell any (remember the [Your Crypto Transactions](#crypto-transactions) section).

**If you really want to use Crypto, use Monero which is the only one with reasonable privacy/anonymity.**

Ideally, you should find a way to buy/sell crypto with cash from an unknown person.

**What about those mobile-only apps (WhatsApp/Signal)**

There are only three ways of securely using those anonymously (that we would recommend). Using a VPN on your phone is not one of those ways. All of those are, unfortunately, "tedious" to say the least.

- Use an Android Emulator within the Windows VM and run the App through your multi-layer of Tor/VPN. The drawback is that such emulators are usually quite resource-hungry and will slow down your VM and use more battery. Here is also an (outdated) guide on this matter: <https://www.bellingcat.com/resources/how-tos/2018/08/23/creating-android-open-source-research-device-pc/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bellingcat.com/resources/how-tos/2018/08/23/creating-android-open-source-research-device-pc/)</sup>. As for myself, we will recommend the use of:

    - Android-x86 on Virtualbox (see <https://www.android-x86.org/documentation/virtualbox.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.android-x86.org/documentation/virtualbox.html)</sup>) that you can also set up easily.

    - AnBox (<https://anbox.io> <sup>[[Archive.org]](https://web.archive.org/web/https://anbox.io/)</sup>) that you can also set up rather easily including on the Whonix Workstation, see <https://www.whonix.org/wiki/Anbox> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Anbox)</sup>

- **Not recommended:** Using a non-official app (such as Wassapp for WhatsApp) to connect from the Windows VM to the app. Use at your own risk as you could get banned for violating the terms of services by using a non-official App.

- **Not recommended and most complicated:** Have a burner Smartphone that you will connect to the VM layered network through Tethering/Sharing of the connection through Wi-Fi. We will not detail this here, but it is an option.

There is no way to reliably set a decent multi-layered connectivity approach easily on an Android phone (it is not even possible on IOS as far as we know). By reliable, we mean being sure that the smartphone will not leak anything such as geolocation or anything else from booting up to shutting down.

**Anything else**

You should use the same logic and security for any other platform.

It should work in most cases with most platforms. **The hardest platform to use with full anonymity is Facebook.**

This will obviously not work with banks and most financial platforms (such as PayPal or Crypto Exchanges) requiring actual real official and existing identification. This guide will not help you there as this would be illegal in most places.

