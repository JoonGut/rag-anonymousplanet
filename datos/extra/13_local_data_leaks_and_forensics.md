## Local Data Leaks and Forensics { #local-data-leaks }

Most of you have probably seen enough Crime dramas on Netflix or TV to know what forensics are. These are technicians (usually working for law enforcement) that will perform various analysis of evidence. This of course could include your smartphone or laptop.

While these might be done by an adversary when you already got "burned", these might also be done randomly during a routine control or a border check. These unrelated checks might reveal secret information to adversaries that had no prior knowledge of such activities.

Forensics techniques are now very advanced and can reveal a staggering amount of information from your devices even if they are encrypted[^253]. These techniques are widely used by law enforcement all over the world and should be considered.

Here are some recent resources you should read about your smartphone:

- UpTurn, The Widespread Power of U.S. Law Enforcement to Search Mobile Phones <https://www.upturn.org/reports/2020/mass-extraction/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.upturn.org/reports/2020/mass-extraction/)</sup>

- New-York Times, The Police Can Probably Break Into Your Phone <https://www.nytimes.com/2020/10/21/technology/iphone-encryption-police.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.nytimes.com/2020/10/21/technology/iphone-encryption-police.html)</sup>

- Vice, Cops Around the Country Can Now Unlock iPhones, Records Show <https://www.vice.com/en/article/vbxxxd/unlock-iphone-ios11-graykey-grayshift-police> <sup>[[Archive.org]](https://web.archive.org/web/https://www.vice.com/en/article/vbxxxd/unlock-iphone-ios11-graykey-grayshift-police)</sup>

I also highly recommend that you read some documents from a forensics examiner perspective such as:

- EnCase Forensic User Guide, <http://encase-docs.opentext.com/documentation/encase/forensic/8.07/Content/Resources/External%20Files/EnCase%20Forensic%20v8.07%20User%20Guide.pdf> <sup>[[Archive.org]](https://web.archive.org/web/http://encase-docs.opentext.com/documentation/encase/forensic/8.07/Content/Resources/External%20Files/EnCase%20Forensic%20v8.07%20User%20Guide.pdf)</sup>

- FTK Forensic Toolkit, <https://accessdata.com/products-services/forensic-toolkit-ftk> <sup>[[Archive.org]](https://web.archive.org/web/https://accessdata.com/products-services/forensic-toolkit-ftk)</sup>

- SANS Digital Forensics and Incident Response Videos, <https://www.youtube.com/c/SANSDigitalForensics/videos>

And finally, here is this very instructive detailed paper on the current state of IOS/Android security from the John Hopkins University: https://securephones.io/main.html[^254].

When it comes to your laptop, the forensics techniques are many and widespread. Many of those issues can be mitigated by using full disk encryption, virtualization (See [Virtualization](#virtualization)), and compartmentalization. This guide will later detail such threats and techniques to mitigate them.

