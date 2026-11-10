## Your CPU { #cpu }

All modern CPUs[^102] are now integrating hidden management platforms such as the now infamous Intel Management Engine (IME)[^103] and the AMD Platform Security Processor (PSP)[^104].

Those management platforms are small operating systems running directly on your CPU as long as they have power. These systems have full access to your computer's network and could be accessed by an adversary to de-anonymize you in various ways (using direct access or using malware for instance) as shown in this enlightening video: BlackHat, How to Hack a Turned-Off Computer, or Running Unsigned Code in IME <https://www.youtube.com/watch?v=9fhNokIgBMU> <sup>[[Invidious]](https://yewtu.be/watch?v=mYsTBPqbya8)</sup>.

These have already been affected by several security vulnerabilities in the past[^105] that allowed malware to gain control of target systems. These are also accused by many privacy actors including the EFF and Libreboot of being a backdoor into any system[^106].

There are some not so straightforward ways[^107] to disable the IME on some CPUs and you should do so if you can. For some AMD laptops, you can disable it within the BIOS settings by disabling PSP.

Note that, to AMD's defense, there were no security vulnerabilities found for ASP and no backdoors either. See <https://www.youtube.com/watch?v=bKH5nGLgi08&t=2834s> <sup>[[Invidious]](https://yewtu.be/watch?v=bKH5nGLgi08&t=2834s)</sup>. In addition, AMD PSP does not provide any remote management capabilities contrary to IME.

If you are feeling a bit more adventurous, you could install your own BIOS using Coreboot[^108] or Libreboot (a distribution of Coreboot) if your laptop supports it. Coreboot allows you to add your own microcode or other firmware blobs in order for the machine to function, but this is based upon user choice, and as of Dec 2022, Libreboot has adopted a similar pragmatic approach in order to support newer devices in the Coreboot tree. (Thanks, kind Anon who corrected previous information in this paragraph.)

Check yourself:

- If you are using Linux you can check the vulnerability status of your CPU to Spectre/Meltdown attacks by using <https://github.com/speed47/spectre-meltdown-checker> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/speed47/spectre-meltdown-checker)</sup> which is available as a package for most Linux distros including Whonix. Spectre is a transient execution attack. There is also PoC code for Spectre v1 and v2 on iPhone devices here: <https://github.com/cispa/BranchDifferent> <sup>[[Archive.org]](https://web.archive.org/web/20220814122148/https://github.com/cispa/BranchDifferent)</sup> and here <https://misc0110.net/files/applespectre_dimva22.pdf> <sup>[[Archive.org]](https://web.archive.org/web/20220814122652/https://misc0110.net/files/applespectre_dimva22.pdf)</sup>

- If you are using Windows, you can check the vulnerability status of your CPU using inSpectre <https://www.grc.com/inspectre.htm> <sup>[[Archive.org]](https://web.archive.org/web/https://www.grc.com/inspectre.htm)</sup>

Some CPUs have unfixable flaws (especially Intel CPUs) that could be exploited by various malware. Here is a good current list of such vulnerabilities affecting recent widespread CPUs: <https://en.wikipedia.org/wiki/Transient_execution_CPU_vulnerability> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Transient_execution_CPU_vulnerability)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Transient_execution_CPU_vulnerability)</sup>

Some of these can be avoided using Virtualization Software settings that can mitigate such exploits. See this guide for more information [Spectre/Meltdown Hardening](https://www.whonix.org/wiki/Spectre_Meltdown) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Spectre_Meltdown)</sup> (warning: these can severely impact the performance of your VMs).

This guide won't go too deep into side-channel and microarchitecture attacks but we will highlight some issues with both Intel and AMD CPU architectures that will be mitigated throughout. It's important to recognize hardware is just as susceptible to bugs, and therefore exploitation, regardless of manufacturer.

We will mitigate some of these issues in this guide by recommending the use of virtual machines on a dedicated anonymous laptop for your sensitive activities that will only be used from an anonymous public network.

**In addition, we recommend the use of AMD CPUs instead of Intel CPUs. See [Types of CPU attacks](#cpu-attacks) for more information.**

- CPU vulnerabilities found in the past few years:

    - [Meltdown](https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability))
    - [Spectre](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability))
    - [Æpic](https://aepicleak.com/)
    - [SGAxe](https://en.wikipedia.org/wiki/Software_Guard_Extensions#SGAxe)
    - [LVI](https://en.wikipedia.org/wiki/Software_Guard_Extensions#LVI)
    - [Plundervolt](https://en.wikipedia.org/wiki/Software_Guard_Extensions#Plundervolt)
    - [MicroScope replay attack](https://en.wikipedia.org/wiki/Software_Guard_Extensions#MicroScope_replay_attack)
    - [Enclave](https://en.wikipedia.org/wiki/Software_Guard_Extensions#Enclave_attack)
    - [Prime+Probe](https://en.wikipedia.org/wiki/Software_Guard_Extensions#Prime+Probe_attack)
    - [Crosstalk](https://www.vusec.net/projects/crosstalk/)
    - [Hertzbleed](https://en.wikipedia.org/wiki/Hertzbleed)
    - [Squip attack](https://www.securityweek.com/amd-processors-expose-sensitive-data-new-squip-attack/)
    - [Zenbleed](https://lock.cmpxchg8b.com/zenbleed.html)

