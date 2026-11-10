# Recover capability before declaring a blocker

Use this for access-dependent work, not as startup ceremony for every task. Prefer a suitable connected tool or verified CLI/API over taking control of the desktop. Follow the user's explicit tool choice and actual tool documentation.

## CLI and cloud

1. Reuse relevant repository runbooks and recent successful session evidence. Check the executable with `command -v`/`whence`, known installation locations and relevant shell initialization. A missing PATH entry, moved SDK or expired temporary directory does not establish missing cloud access. Keep the search bounded to plausible locations; do not scan the whole home directory or read credential stores.
2. Verify the located executable/version and required runtime. If the SDK is truly absent, distinguish recovery/install needs from authentication. Use an existing supported alternate tool or the normal authorized installation mechanism; do not silently install packages, copy browser credentials, export tokens or change global configuration to manufacture access.
3. Check the active account and explicit target project/environment with non-secret metadata. CLI login and Application Default Credentials are different mechanisms: missing ADC does not invalidate a working CLI login. Follow execution permissions. Route every `acli` invocation and all Jira access through `jira-ticket-supporter`, which owns its discovery, authentication and execution rules.
4. Try the smallest relevant read. Classify the failed layer: executable/runtime, sandbox/network, authentication, account prerequisite, target/project or resource IAM. A generic 403 is not proof of a missing role; inspect its service error and relevant prerequisites, including account terms when indicated. Never accept terms on the user's behalf or widen permissions to test a theory. A confirmed denial remains a real boundary.
5. Report exactly what was attempted, what succeeded, and the remaining failed layer. Share capability facts with workers so they do not rediscover access independently. Old success establishes a useful lead, not current access or authority.

## Existing cloud patterns

When the user names reference applications, inspect their relevant current configuration before designing or provisioning. Reconcile environments, branch/deployment triggers, manual production promotion, serving revision/image, identity, hosting/domain wiring and resource ownership only as needed for this task. Prefer adapting the verified pattern; explain any necessary deviation before it creates rework. Application migration does not imply ownership of another team's provisioning or permission changes.

## Browser fallback

Verify the API/CLI/connector capability for the needed operation; do not assume every UI action has a command equivalent. Jira access remains exclusively with `jira-ticket-supporter`; this generic fallback does not permit another Jira client. If a browser is needed, choose a documented agent-owned instance or independent connection, such as an isolated in-app browser when available. Verify independence rather than assuming a session label, hidden flag or new tab isolates the user's foreground browser. Do not use their active profile or desktop session without their explicit choice. Ask for sign-in only in the selected independent surface when necessary; never copy credentials between profiles. If no independent route works, state that specific access gap, not that the service is universally unavailable.

Maintain one owner for each mutating resource and close only agent-owned surfaces. Separate browser sessions still share application data and must coordinate writes.
