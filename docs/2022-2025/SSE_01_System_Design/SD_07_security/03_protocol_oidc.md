# OIDC
## Overview
```
SP (sp1, sp2, sp3, ...) <-- SSO ( using some protocol ) --> IDP
```
- SSO concepts.
- oidc is one of the protocol for SSO
- other protocol for SSo : `SAML, WS-F`
- oidc came as additional layer ontop for existing OAuth to handle Authentication scenario.
  - authz with idp first, using single credential
  - then, request authz access token.
  - same req, just pass one more scope: `openid`

