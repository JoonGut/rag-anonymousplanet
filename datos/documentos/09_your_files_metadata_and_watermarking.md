## Your files, documents, pictures, and videos { #your-files }

### Properties and Metadata { #file-metadata }

This can be obvious to many but not to all. Most files have metadata attached to them. Good examples are pictures that store EXIF[^222] information which can hold a lot of information such as GPS coordinates, which camera/phone model took it, and when it was taken precisely. While this information might not directly give out who you are, it could tell exactly where you were at a certain moment which could allow others to use various sources to find you (CCTV or other footage taken at the same place at the same time during a protest for instance). You must verify any file you would put on those platforms for any properties that might hold any information that might lead back to you.

Here is an example of EXIF data that could be on a picture:

![](../media/image13.png)

(Illustration from Wikipedia)

This also works for videos. Yes, videos too have geo-tagging, and many are very unaware of this. Here Is for instance a very convenient tool to geo-locate YouTube videos: <https://mattw.io/youtube-geofind/location> <sup>[[Archive.org]](https://web.archive.org/web/https://mattw.io/youtube-geofind/location)</sup>

For this reason, you will always have to be incredibly careful when uploading files using your anonymous identities and check the metadata of those files.

**Even if you publish a plain text file, you should always double or triple-check it for any information leakage before publishing. You will find some guidance about this in the [Some additional measures against forensics](#anti-forensics) section at the end of the guide.**

### Watermarking { #watermarking }

#### Pictures, Video and Audio { #media-watermarking }

Pictures/Videos often contain visible watermarks indicating who is the owner/creator but there are also invisible watermarks in various products aiming at identifying the viewer itself.

So, if you are a whistleblower and thinking about leaking some picture/audio/video file. Think twice. There are chances that those might contain invisible watermarking within them that would include information about you as a viewer. Such watermarks can be enabled with a simple switch in like Zoom (Video[^223] or Audio[^224]) or with extensions[^225] for popular apps such as Adobe Premiere Pro. These can be inserted by various content management systems.

For a recent example where someone leaking a Zoom meeting recording was caught because it was watermarked: <https://theintercept.com/2021/01/18/leak-zoom-meeting/> <sup>[[Tor Mirror]](http://27m3p2uv7igmj6kvd4ql3cct5h3sdwrsajovkkndeufumzyfhlfev4qd.onion/2021/01/18/leak-zoom-meeting/)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://theintercept.com/2021/01/18/leak-zoom-meeting/)</sup>

Such watermarks can be inserted by various products[^226]'[^227]'[^228]'[^229] using Steganography[^230] and can resist compression[^231] and re-encoding[^232]'[^233].

These watermarks are not easily detectable and could allow identification of the source despite all efforts.

In addition to watermarks, the camera used for filming (and therefore the device used for filming) a video can also be identified using various techniques such as lens identification[^234] which could lead to de-anonymization.

Be extremely careful when publishing videos/pictures/audio files from known commercial platforms as they might contain such invisible watermarks in addition to details in the images themselves. There is no guaranteed 100% protection against those. You will have to use common sense.

#### Printer Watermarking { #printer-watermarking }

Did you know your printer is most likely spying on you too? Even if it is not connected to any network? This is usually a known fact by many people in the IT community but few outside people.

Yes ... Your printers can be used to de-anonymize you as well as explained by the EFF here <https://www.eff.org/issues/printers> <sup>[[Archive.org]](https://web.archive.org/web/https://www.eff.org/issues/printers)</sup>

With this (old but still relevant) video explaining how from the EFF as well: <https://www.youtube.com/watch?v=izMGMsIZK4U> <sup>[[Invidious]](https://yewtu.be/watch?v=izMGMsIZK4U)</sup>

Many printers will print an invisible watermark allowing for identification of the printer on every printed page. This is called Printer Steganography[^235]. There is no tangible way to mitigate this but to inform yourself on your printer and make sure it does not print any invisible watermark. This is important if you intend to print anonymously.

Here is an (old but still relevant) list of printers and brands who do not print such tracking dots provided by the EFF <https://www.eff.org/pages/list-printers-which-do-or-do-not-display-tracking-dots> <sup>[[Archive.org]](https://web.archive.org/web/https://www.eff.org/pages/list-printers-which-do-or-do-not-display-tracking-dots)</sup>

Here are also some tips from the Whonix documentation ([Printing and Scanning](https://www.whonix.org/wiki/Printing_and_Scanning)) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Printing_and_Scanning)</sup>:

**Do not ever print in Color, usually, watermarks are not present without color toners/cartridges**[^236]**.**

### Pixelized or Blurred Information { #pixelized-info }

Did you ever see a document with blurred text? Did you ever make fun of those movies/series where they "enhance" an image to recover seemingly impossible-to-read information?

Well, there are techniques for recovering information from such documents, videos, and pictures.

Here is for example an open-source project you could use yourself for recovering text from some blurred images yourself: <https://github.com/beurtschipper/Depix> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/beurtschipper/Depix)</sup>

![image14](../media/image14.png)

This is of course an open-source project available for all to use. But you can imagine that such techniques have probably been used before by other adversaries. These could be used to reveal blurred information from published documents that could then be used to de-anonymize you.

There are also tutorials for using such techniques using Photo Editing tools such as GIMP such as <https://medium.com/@somdevsangwan/unblurring-images-for-osint-and-more-part-1-5ee36db6a70b>   <sup>[[Archive.org]](https://web.archive.org/web/https://medium.com/@somdevsangwan/unblurring-images-for-osint-and-more-part-1-5ee36db6a70b)</sup> followed by <https://medium.com/@somdevsangwan/deblurring-images-for-osint-part-2-ba564af8eb5d> <sup>[[Scribe.rip]](https://scribe.rip/@somdevsangwan/deblurring-images-for-osint-part-2-ba564af8eb5d)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://medium.com/@somdevsangwan/deblurring-images-for-osint-part-2-ba564af8eb5d)</sup>

![image15](../media/image15.png)

Finally, you will find plenty of deblurring resources here: <https://github.com/subeeshvasu/Awesome-Deblurring> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/subeeshvasu/Awesome-Deblurring)</sup>

Some online services could even help you do this automatically to some extent like MyHeritage.com enhance tool:

<https://www.myheritage.com/photo-enhancer> <sup>[[Archive.org]](https://web.archive.org/web/https://www.myheritage.com/photo-enhancer)</sup>

Here is the result of the above image:

![image16](../media/image16.png)

Of course, this tool is more like "guessing" than really deblurring at this point, but it could be enough to find you using various reverse image searching services.

There are also techniques to deblur/depixelate parts in videos: see <https://positive.security/blog/video-depixelation> <sup>[[Archive.org]](https://web.archive.org/web/https://positive.security/blog/video-depixelation)</sup>

For this reason, it is always extremely important that you correctly redact and curate any document you might want to publish. Blurring is not enough, and you should always completely blacken/remove any sensitive data to avoid any attempt at recovering data from any adversary. Do not pixelized, do not blur, just put a hard black rectangle to redact information.

