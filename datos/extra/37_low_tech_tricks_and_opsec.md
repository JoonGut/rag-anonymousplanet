# Some low-tech old-school tricks { #low-tech-tricks }

## Hide Communications in Plain Sight { #steganography }

You must keep in mind that using all those security measures (encryption, plausible deniability, VPN, tor, secure operating systems ...) can make you suspicious just by using them. Using could be the equivalent of stating openly "I something to hide" to an observer which could then motivate some adversaries to investigate/survey you further.

So, there are other ways you could exchange or send messages online to others in case of need without disclosing your identity or establishing direct communication with them. These have been in use by various organizations for decades and can be of help if you do not want to attract attention by using secure tech while still communicating some sensitive information without attracting attention.

A commonly used technique that combines the idea of a Dead Drop[^451] and Secure Communication Obfuscation[^452] through Steganography[^453] and/or Kleptography[^454] and has many names such as Koalang[^455] or "Talking Around" or even "Social Steganography". This technique is very old and still widely used nowadays by teenagers to bypass parental control. It is hiding in plain sight.

Here is one example if you want to let someone know something is wrong and they should go dark? That they should immediately wipe all their data, get rid of their burner phones and sensitive information?

What if you want to let someone you trust (friends, family, lawyers, journalists ...) know that you are in trouble, and they should look out for you?

All this without revealing the identity of the person you are sending the message to nor disclosing the content of that message to any third party and without raising suspicions and without using any of the secure methods mentioned above.

Well, you could just use any online public platform for this (Instagram, Twitter, Reddit, any forum, YouTube ...) by using in-context (of the chosen platform/media) agreed upon (between you and your contact) coded messages that only your contact would understand.

This could be a set of specific emojis or a specifically worded mundane comment. Or even just a like on a specific post from a known influencer you usually watch and like. While this would look completely normal to anyone, this could mean a lot to a knowledgeable reader who could then take appropriate agreed-upon actions. You could also hide the message using Steganography using for instance <https://stegcloak.surge.sh/>.

You do not even have to go that far. A simple "Last seen" time on a specific account could be enough to trigger a message agreed upon. If your interlocutor sees that this account was online. It could mean there is an issue.

## How to spot if someone has been searching your stuff { #detect-searching }

There are some old tricks that you can use to spot if people have been messing with your stuff while you were away.

One trick for instance is quite simple and just requires a wire/cable. Simply lay objects on your desk/night table or in your drawers following a straight line. You can use a simple USB cable as a tool to align them.

Make a line with your cable and place objects along the line. When you are back, just check those places and check if the objects are still placed along the line. This allows you not to remember precisely where your things were without taking pictures.

Fortunately, modern technology has made this even simpler. If you suspect someone might be looking through your stuff while you are away, you can just take a picture of the area with your phone before leaving. When you are back, just compare the areas with your pictures and everything should be exactly where you left it. If anything moved, then someone was there.

It will be extremely hard and time-consuming for an adversary to search through your stuff and then replace it exactly as you left it with complete precision.

What if it is a printed document or book and you want to know if someone read it? Even simpler. Just carefully make a note within the document with a pencil. And then erase it with any pencil eraser as if you wanted to correct it. The trick is to carefully leave the eraser traces/residues on the area you erased/pencil written areas and close the document. You could also take a picture of the residues before closing the document.

Most likely if someone went through your document to read it and re-placed it carefully, this residue will fall off or be moved significantly. It is a simple old-school trick that could tell you someone searched a document you had.

# Some last OPSEC thoughts { #opsec-thoughts }

Wait, what is OPSEC? Well, OPSEC means Operations Security[^456]. The basic definition is: "OPSEC is the process of protecting individual pieces of data that could be grouped together to give the bigger picture."

The important step here, and probably the easiest one, is a lesson you can take from the movie Fight Club: the first rule is that you **do not** talk about Fight Club. This applies to many aspects of your online operational security or OPSEC. Taking your time to go through this guide will reward you with the tools and knowledge to embrace a fuller, more secure experience on the internet. Rest assured that this guide will reveal things to you that will frustrate your enemy. You will learn how to protect your operating systems and lockdown your critical information and ensure mission success. But the one thing you must adhere to is this rule of thumb - do not talk about operation details. The biggest adversarial threat to you is OSINT (discussed below and throughout the document). The enemy will gather information on you based on what they observe about you and your activities online and in real life.

Adversaries take many forms. To some, they are actors of a foreign government, while to others they may be simply a rival company's employee looking to find disgruntled workers to target for further pressuring. To most, the general task of OPSEC is that this is your ship - you must not do anything or say anything to sink your own ship. Simply expressing your frustration with your boss or your work conditions or your equipment, might be enough to generate not only a behavior profile but also a vector of attack. A disgruntled employee, in this example, is what generally provides enough information to warrant pressuring of that employee for further information and possibly even extortion, blackmail, or worse. Failure to implement basic OPSEC can lead to failure at various points. It can lead to serious injury or even death if your threat model is a determined attacker, foreign actor, and so on.

You must live by the simple rule that "loose lips sink ships" - but also that they are usually your lips which will do the sinking. OPSEC is often just applying common sense and being cautious about your activities including in the physical world:

## Digital and Online OPSEC { #digital-opsec }

- **Remember to use passphrases or suits of words instead of short passwords and use a different one for each service. See [Guidelines for passwords and passphrases](#password-guidelines).**

- Make sure you are not keeping a copy of this guide anywhere unsafe after. The sole presence of this guide will most likely defeat all your plausible deniability possibilities.

- OSINT "yourself" and your identities from time to time by looking for them yourself online using various search engines to monitor your online identities. You can even automate the process somewhat using various tools such as Google Alerts <https://www.google.com/alerts> <sup>[[Archive.org]](https://web.archive.org/web/https://www.google.com/alerts)</sup>.

- Do not ever use biometrics alone to safeguard your secrets. Biometrics can be used without your consent.

- Do check the signatures and hashes of software and documents you download before installing/viewing them.

- Do not have the same behavior such as visiting the same links on the clearnet then visit the same with the your anoynous online identity. Watch this DEF CON 25 presentation if you didn't before: [DEF CON 25 - Svea Eckert, Andreas Dewes - Dark Data](https://www.youtube.com/watch?v=1nvYGi7-Lxo) <sup>[[Invidious]](https://yewtu.be/watch?v=1nvYGi7-Lxo)</sup>.

- Encrypt everything but do not take it for granted. Remember the $5 wrench.

## Physical and IRL OPSEC { #physical-opsec }

- Remember to ["Physically Tamper protect your laptop"](#tamper-protection).

- See [Important notes about evil-maid and tampering](#evil-maid-tampering-notes).

- Check out [How to spot if someone has been searching your stuff](#detect-searching).

- Consider the use of Haven <https://guardianproject.github.io/haven/> <sup>[[Archive.org]](https://web.archive.org/web/https://guardianproject.github.io/haven/)</sup> on some old android phone to keep watch on your home/room while you are away.

- Remember [Warning about smartphones and smart devices](#smartphones-warning). Do not forget your smart devices can compromise your anonymity.

- Do not ever travel with those devices if you must pass strong border checks and where they could be illegal or raise suspicion.

- Do not plug any equipment in that laptop unless you trust it. Use a USB data blocker for charging.

- Remember the first rule of fight club and do not talk to anyone about your sensitive activities using your real identity.

- Keep a normal life and do not be weird. If you spend all your online time using Tor to access the internet and have no social network accounts at all ... You are already suspicious and attracting unnecessary attention.

- Keep plausible deniability as an option but remember it will not help against the 5$ wrench either.

- Never ever leave your laptop unattended/on/unlocked anywhere when conducting sensitive activities. Remember the story of Ross Ulbricht and his arrest <https://en.wikipedia.org/wiki/Ross_Ulbricht#Silk_Road,_arrest_and_trial> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Ross_Ulbricht)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Ross_Ulbricht)</sup>.

- Check for tampering regularly (not only your devices but also your home/room).

- If you can, do not talk to the police/authorities (at least if you are in the US) <https://www.youtube.com/watch?v=d-7o9xYp7eE> <sup>[[Invidious]](https://yewtu.be/watch?v=d-7o9xYp7eE)</sup> without a lawyer. Remain silent.

- Know and always have at your disposal the details of a lawyer that could help you as a last resort in case things go wrong.

- Keep your situation awareness high but not too high as to appear suspicious.

- Consider using a physical security key (e.g., YubiCo YubiKey) for various protections against account compromise. **(Not covered in this version of the guide but is a work in progress for later versions.)**

- Read the tips here <https://www.whonix.org/wiki/DoNot> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/DoNot)</sup>

- **Have common sense, do not be dumb, look and learn from others' mistakes, watch/read these:**

    - Medium.com, Darkweb Vendors and the Basic Opsec Mistakes They Keep Making <https://medium.com/@c5/darkweb-vendors-and-the-basic-opsec-mistakes-they-keep-making-e54c285a488c> <sup>[[Scribe.rip]](https://scribe.rip/@c5/darkweb-vendors-and-the-basic-opsec-mistakes-they-keep-making-e54c285a488c)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://medium.com/@c5/darkweb-vendors-and-the-basic-opsec-mistakes-they-keep-making-e54c285a488c)</sup>

    - 2020, Sinwindie, OSINT, and Dark Web Markets, Why OPSEC Still Matters <https://www.youtube.com/watch?v=IqZZU9lFlF4> <sup>[[Invidious]](https://yewtu.be/watch?v=IqZZU9lFlF4)</sup>

    - 2020, RSA Conference 2020, When Cybercriminals with Good OpSec Attack <https://www.youtube.com/watch?v=zXmZnU2GdVk> <sup>[[Invidious]](https://yewtu.be/watch?v=zXmZnU2GdVk)</sup>

    - 2015, DEF CON 22, Adrian Crenshaw, Dropping Docs on Darknets: How People Got Caught <https://www.youtube.com/watch?v=eQ2OZKitRwc> <sup>[[Invidious]](https://yewtu.be/watch?v=eQ2OZKitRwc)</sup> ([Slides](https://www.defcon.org/images/defcon-22/dc-22-presentations/Crenshaw/DEFCON-22-Adrian-Crenshaw-Dropping-Docs-on-Darknets-How-People-Got-Caught-UPDATED.pdf) <sup>[[Archive.org]](https://web.archive.org/web/https://www.defcon.org/images/defcon-22/dc-22-presentations/Crenshaw/DEFCON-22-Adrian-Crenshaw-Dropping-Docs-on-Darknets-How-People-Got-Caught-UPDATED.pdf)</sup>)

    - 2017, Ochko123 - How the Feds Caught Russian Mega-Carder Roman Seleznev <https://www.youtube.com/watch?v=6Chp12sEnWk> <sup>[[Invidious]](https://yewtu.be/watch?v=6Chp12sEnWk)</sup>

    - 2017, [DEF CON 25 - Svea Eckert, Andreas Dewes - Dark Data](https://www.youtube.com/watch?v=1nvYGi7-Lxo) <sup>[[Invidious]](https://yewtu.be/watch?v=1nvYGi7-Lxo)</sup>

    - 2015, DEF CON 22, Zoz, Don't Fuck It Up! <https://www.youtube.com/watch?v=J1q4Ir2J8P8> <sup>[[Invidious]](https://yewtu.be/watch?v=J1q4Ir2J8P8)</sup>

    - 2020, Bad Opsec, How Tor Users Got Caught, <https://www.youtube.com/watch?v=GR_U0G-QGA0> <sup>[[Invidious]](https://yewtu.be/watch?v=GR_U0G-QGA0)</sup>

    - 2022, Master of OpSec Masters: A View Through the Prism of Time, <https://officercia.mirror.xyz/4x2-M4R2cSnID1wpsTO4CQNrMQ5JUFouR-rZ_N4xO-Q> <sup>[[Archive.org]](https://web.archive.org/web/20220714213939/https://officercia.mirror.xyz/4x2-M4R2cSnID1wpsTO4CQNrMQ5JUFouR-rZ_N4xO-Q)</sup>
    - 2022, How can you become a one-man-army OSINT specialist? <https://officercia.mirror.xyz/5KSkJOTgMtvgC36v1GqZ987N-_Oj_zwvGatOk0A47Ws> <sup>[[Archive.org]](https://web.archive.org/web/20220718231735/https://officercia.mirror.xyz/5KSkJOTgMtvgC36v1GqZ987N-_Oj_zwvGatOk0A47Ws)</sup>

It is recommended that you learn about the common ways people mess up OPSEC <https://dan-kir.github.io/2022/05/26/OPSEC-notes.html> <sup>[[Archive.org]](https://web.archive.org/web/20220717064253/https://dan-kir.github.io/2022/05/26/OPSEC-notes.html)</sup>. Whatever you do, take OPSEC seriously, and [Don't Fuck It Up!](https://www.youtube.com/watch?v=J1q4Ir2J8P8)

**FINAL OPSEC DISCLAIMER: KEEP YOUR ANONYMOUS IDENTITIES COMPLETELY SANDBOXED FROM YOUR NORMAL ENVIRONMENT AND REAL IDENTITY. DO NOT SHARE ANYTHING BETWEEN THE ANONYMOUS ENVIRONMENTS AND THE REAL IDENTITY ENVIRONMENT. KEEP THEM COMPLETELY COMPARTMENTALIZED ON EVERY LEVEL. MOST OPSEC FAILURES ARE DUE TO SOMEONE ACCIDENTALLY LEAKING INFORMATION RATHER THAN TECHNICAL FAILURES.**

