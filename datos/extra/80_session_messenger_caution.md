# Session Messenger Caution { #session-messenger-caution }

- They use LokiNet, which requires Oxen to run nodes to route Session traffic, and it costs 15,000 \$OXEN or 3,750 \$OXEN for a shared node[^538], which is about \~\$1,800 US dollars or \~\$500 US dollars, respectively. This high cost creates a barrier to entry for running nodes, potentially centralizing the network and limiting its accessibility.
    - The price of running nodes essentially puts their network behind a paywall if you want to run a node, even just to contribute bandwidth to the network like you might with Tor. But there is a stakeless fork of Lokinet.
    - Session's developers claim this to be an attempt to prevent [sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack), but many have argued that this only encourages such attacks; by doing so, guaranteeing only governments and other well-funded organizations (the people these networks normally try to protect against) will ever have the financial resources to run nodes. (Eh, it's all pretty debatable. But $OXEN is privacy-focused.)
- They dropped critical security features of their protocol (perfect forward secrecy (PFS) and deniability)[^418] in favor of long-term message keys and self-deleting cryptographic signatures, which provide much weaker security guarantees. [^539]
    - This _might_ not be as bad, if the nodes are free to run, but they're not.
- April 2021: Session was audited[^419] with satisfactory results, but that audit does not mention these changes. We also currently lack sufficient information on LokiNet (the onion routing network used by Session) to endorse it. Session is still recommended by some, for example Techlore.[^420]
- Their funding is completely opaque.

In short, our opinion is that you may use Session Messenger on iOS due to the absence of a better alternative (such as Briar). But if Briar or another app (maybe Cwtch in the future) becomes available, we will recommend going away from Session messenger as soon as possible. It is a last resort.

