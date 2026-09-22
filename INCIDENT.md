# Incident: planted token detected by gitleaks (Lab 6 drill)

## What happened
A fake GHCR token string was committed to throwaway_leak.txt
and caught by a local gitleaks scan before it reached a shared branch.

## Response (in order — this order is not negotiable)

1. ROTATE FIRST. Treat the token as burned the moment it was
   committed, even locally, even before any push. Revoke it at
   the source (GitHub → Settings → Developer settings → Tokens)
   and issue a replacement. Rotate related tokens too — assume
   lateral discovery, not just this one credential.

2. CLEAN HISTORY SECOND, only after rotation. Remove the file,
   rewrite history if it already reached a shared branch
   (git filter-repo or BFG), and force-push with the team's
   awareness. Deleting the commit does NOT un-leak a live
   credential — it only cleans up evidence after the credential
   is already safe.

3. Add gitleaks as a required CI check so this class of leak
   cannot merge silently again.
