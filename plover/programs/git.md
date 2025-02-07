# Git Command Dictionary

## Git Vocabulary

```yaml
TKPWUB                      :  GitHub
AZ/SHUR                     :  Azure
TKPWHRAB                    :  GitLab
TKPWEUT                     :  git
```

## Custom Commands

```yaml
KR*D/TKPW*EUT               :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
KR*D/TKPWEUT                :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
TKPW*EUT/HO*EPL             :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
TKPWUB/TKPWUB               :  https://github.com/{^}
TKPWUB/TKPWUB/TKPWUB        :  "git@github.com:{^}"
ST*TS                       :  status
TKPWEUT/TKEUF               :  git diff
TKPW*EUF                    :  git diff
TKPWA*P                     :  add .
TKPWEUT/ST*TS               :  git status
TKPWEUT/TKPWEUT             :  git status\\n{^}
PHERPBLG                    :  merge
TKPWEUT/TKEUF/H-PBZ/KAERBD  :  git diff --cached
TKPWEUT/KPHEUT/H-PBS/SR*    :  git commit -v
TKPWEUT/KHEBG/O*UT          :  git checkout
TKPWEUT/KHEBGT/PW*          :  git checkout -b{^ ^}
KH*EBGT : git checkout {^ ^}
KH*EBGT/KH*EBGT : git checkout -b{^ ^}{MODE:SNAKE} # Fancy checkout new branch with snake case
TKPWEUT/PHERPBLG            :  git merge
TKEUF                       :  diff
TKEUF/H-PBZ/KAERBD          :  diff --cached
KPHEUT/H*PB/SR*             :  commit -v
PURB/O*RPBLG/PHAFRT         :  push origin master
PUL/H-PBZ/RE/PWAEUS         :  pull --rebase
HROG/H*PB/P*                :  log -p
RE/SET/KPA*E/HED/KR-RT      :  reset HEAD ^
```

```yaml
TKPW*EUFT : {^}git fetch upstream
TKPW*EUPLT: {^}git commit --amend
TKPW*EUPLTD: {^}git commit --amend --no-edit
TKPWEUP: {^git push\\n}
TKPWEUT/PURB/PURB: {^}git push -u origin --all
TKPWEUT/PURB/O*RPBLG: {^}git push -u origin --all
TKPWEUT/PURB/PWRAFRPB: {^}git push --set-upstream origin $(git symbolic-ref HEAD --short)
TKPWEUPL: {^}git pull\\n
TKPW*EUPL: {^}git pull --rebase
TRAO*EU : --dry-run
TKPW*EUTD/TKRAOEU: {^}git add --verbose . --dry-run
TKPW*EUTD: {^}git add --verbose .
TKPWEUTS: {^git status --short\\n}
TKPWEUT/KEUG/HR*EUS: {^}git config --list
TKPWEUT/TPH*EUT: {^}git init
TKPWEUTD: {^}git add --verbose **{\#LEFT}{^}
TKPW*EUFRB: {^}git stash
TKPWA*RB: {^}git stash
TKPWO*P: {^}git stash pop
TKPWOP: {^}git stash pop
TKPWEUT/STARB: {^}git stash
TKPWEUT/STARB/POP: {^}git stash pop
TKPWEUT/STARB/PURB: {^}git stash push
TKPW*EUL: {^}git log --oneline --decorate --all --graph
TKPW*EULG: {^}git log --oneline --decorate --all --graph
TKPWEUT/HRO*G: {^}git log --oneline --decorate --all --graph
TKPWEUT/HROG: {^}git log
STA*RS: {^}**{\#LEFT}{^}
TKPWEUT/KHEUBG : git cherry-pick
```
## Git Worktrees

```yaml
TKPWRAO*E : git worktree
```

## Dot files git commands

```yaml
TK*EUPLT: {^}dot commit --message=\"{^}
TK*EUPLTD: {^}dot commit --all --message=\"{^}
TK*EUP: {^}dot push
TK*EUPL: {^}dot pull
TK*EUTS: {^}dot status
TK*EUL: {^}dot log --oneline --decorate --all --graph
TKEUTD: {^}dot add --verbose **}{\#LEFT}{^}
TK*EUTD: {^}dot add --verbose .
```

## Commands from Paul Fioravanti's dictionary

```PaulsGit
"TKPW*EUD": "{^git diff --ignore-all-space}"                                                                                      # GIt Diff
"TKPW*EUFP": "{^git add --patch}"                                                                                                 # GIt add patCH [override]
"TKPW*EUFPT": "{^git checkout --force}"                                                                                           # GIt CHeckouT (force)
"TKPW*EUFRPB": "{^git branch --delete}"                                                                                           # GIt braNCH (delete)
"TKPW*EUL": "{^git log --oneline --decorate --all --graph}"                                                                       # GIt Log
"TKPW*EULG": "{^git log --oneline --decorate --all --graph}"                                                                      # GIt LoG
"TKPW*EUP": "{^git push --force}"                                                                                                 # GIt Push (force) [override]
"TKPW*EUP/O*RPBLG/PWRA*FRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                       # GIt Push (force) ORIGIN (current BRANCH name)
"TKPW*EUPL": "{^git pull --rebase}"                                                                                               # GIt PuLL (rebase) [override]
"TKPW*EUPL/O*RPBLG/PHAEUPB": "{^git pull --rebase origin main}"                                                                   # GIT PULL (rebase) ORIGIN MAIN
"TKPW*EUPL/O*RPBLG/PHAFRT": "{^git pull --rebase origin master}"                                                                  # GIT PULL (rebase) ORIGIN MASTER
"TKPW*EUPL/O*RPBLG/PWRAFRPB": "{^git pull --rebase origin $(git symbolic-ref HEAD --short)}"                                      # GIT PULL (rebase) ORIGIN (current BRANCH name)
"TKPW*EUPL/STPRAOEPL/PHAEUPB": "{^git pull --rebase upstream main}"                                                               # GIT PULL (rebase) uPSTREAM MAIN
"TKPW*EUPL/STPRAOEPL/PHAFRT": "{^git pull --rebase upstream master}"                                                              # GIT PULL (rebase) uPSTREAM MASTER
"TKPW*EUPL/STPRAOEPL/PWRAFRPB": "{^git pull --rebase upstream $(git symbolic-ref HEAD --short)}"                                  # GIT PULL (rebase) uPSTREAM (current BRANCH name)
"TKPW*EURBS": "{^git rebase --interactive}"                                                                                       # Git ReBaSe (interactive)
"TKPW*EURPL": "{^git rm --force}"                                                                                                 # GIt RM (force)
"TKPW*EURPLT": "{^git remote --verbose}"                                                                                          # GIt ReMoTe (verbose)
"TKPW*EUTD": "{^git add .}"                                                                                                       # GIT aDD (current pathspec)
"TKPW*EUTS": "{^git status --short}"                                                                                              # GIT Status (short)
"TKPW*URB": "{^git stash push}"                                                                                                   # Git stash pUSH
"TKPWA*FP": "{^git add --patch}"                                                                                                  # Git Add patCH
"TKPWAO*EB": "{^git rebase --abort}"                                                                                              # Git rEBase abort
"TKPWAOEB": "{^git rebase}"                                                                                                       # Git rEBase
"TKPWAOEBT": "{^git rebase --continue}"                                                                                           # Git rEBase conTinue
"TKPWEUD": "{^git diff}"                                                                                                          # GIt Diff
"TKPWEUFP": "{^git add --patch}"                                                                                                  # GIt add patCH [override]
"TKPWEUFPT": "{^git checkout}"                                                                                                    # GIt CHeckouT
"TKPWEUFPT/PW*": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}}"                                                            # GIt CHeckouT Branch
"TKPWEUFPT/PWRAFRPB": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                        # GIt CHeckouT BRANCH
"TKPWEUFPTD": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                                # GIt CHeckouT (branch)
"TKPWEUFRB": "{^git stash}"                                                                                                       # GIt StaSH
"TKPWEUFRPB": "{^git branch --list --verbose}"                                                                                    # GIt braNCH
"TKPWEUP": "{^git push}"                                                                                                          # GIt Push
"TKPWEUP/O*RPBLG/PWRAFRPB": "{^git push origin $(git symbolic-ref HEAD --short)}"                                                 # GIT PUSH ORIGIN (current BRANCH name)
"TKPWEUPBT": "{^git init}"                                                                                                        # GIt iNiT
"TKPWEUPL": "{^git pull}"                                                                                                         # GIt PuLL [override]
"TKPWEUPL/O*RPBLG/PHAEUPB": "{^git pull origin main}"                                                                             # GIt PuLL ORIGIN MAIN
"TKPWEUPL/O*RPBLG/PHAFRT": "{^git pull origin master}"                                                                            # GIt PuLL ORIGIN MASTER
"TKPWEUPL/O*RPBLG/PWRAFRPB": "{^git pull origin $(git symbolic-ref HEAD --short)}"                                                # GIt PuLL ORIGIN (current BRANCH name)
"TKPWEUPL/STPRAOEPL/PHAEUPB": "{^git pull upstream main}"                                                                         # GIt PuLL uPSTREAM MAIN
"TKPWEUPL/STPRAOEPL/PHAFRT": "{^git pull upstream master}"                                                                        # GIt PuLL uPSTREAM MASTER
"TKPWEUPL/STPRAOEPL/PWRAFRPB": "{^git pull upstream $(git symbolic-ref HEAD --short)}"                                            # GIt PuLL uPSTREAM (current BRANCH name)
"TKPWEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                           # GIt coMMiT (message)
"TKPWEUPLTD": "{^git commit --all --message=\"\"^}{#LEFT}{-|}"                                                                    # GIt coMMiT (all, message)
"TKPWEURBS": "{^git rebase}"                                                                                                      # Git ReBaSe
"TKPWEURBS/PWORT": "{^git rebase --abort}"                                                                                        # Git ReBaSe ABORT
"TKPWEURBS/T-PB": "{^git rebase --continue}"                                                                                      # Git ReBaSe CONTINUE
"TKPWEURPBLG": "{^git merge}"                                                                                                     # GIt meRGe
"TKPWEURPL": "{^git rm}"                                                                                                          # GIt RM
"TKPWEURPLT": "{^git remote}"                                                                                                     # GIt ReMoTe
"TKPWEUT/A*D": "{^git add .}"                                                                                                     # GIT ADd (current pathspec)
"TKPWEUT/AD/AD": "{^git add .}"                                                                                                   # GIT ADD (current pathspec)
"TKPWEUT/AD/PAFP": "{^git add --patch}"                                                                                           # GIT ADD PATCH
"TKPWEUT/HRO*G": "{^git log --oneline --decorate --all --graph}"                                                                  # GIT LOG (oneline decorate all graph)
"TKPWEUT/HROG": "{^git log}"                                                                                                      # GIT LOG
"TKPWEUT/KHO*UT": "{^git checkout --force}"                                                                                       # GIT CHECKOUT force
"TKPWEUT/KHOUT/PW*": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                         # GIT CHECKOUT Branch
"TKPWEUT/KHOUT/PWRAFRPB": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                    # GIT CHECKOUT BRANCH
"TKPWEUT/KHOUT/TPORS": "{^git checkout --force}"                                                                                  # GIT CHECKOUT FORCE
"TKPWEUT/KHR*UP": "{^git branch --merged | grep --invert-match '\\*\\|master\\|develop\\|main' | xargs -n 1 git branch --delete}" # GIT CLEANUP
"TKPWEUT/KPH*EUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                   # GIT CoMMIT Message
"TKPWEUT/KPH*EUT": "{^git commit --amend}"                                                                                        # GIT CoMMIT (amend)
"TKPWEUT/KPH*EUTD": "{^git commit --amend --no-edit}"                                                                             # GIT CoMMIT (amend) no-eDit
"TKPWEUT/KPHEUFPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                   # GIT CoMMIT Message
"TKPWEUT/KPHEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                    # GIT CoMMIT Message
"TKPWEUT/KPHEUT": "{^git commit}"                                                                                                 # GIT CoMMIT
"TKPWEUT/KPHEUT/APLD": "{^git commit --amend}"                                                                                    # GIT CoMMIT AMEND
"TKPWEUT/KPHEUT/APLD/TPHO*ETD": "{^git commit --amend --no-edit}"                                                                 # GIT CoMMIT AMEND NO EDIT
"TKPWEUT/KPHEUT/APLD/TPHO/ETD": "{^git commit --amend --no-edit}"                                                                 # GIT CoMMIT AMEND NO EDIT
"TKPWEUT/KPHEUT/PHEPBLG": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                              # GIT CoMMIT MESSAGE
"TKPWEUT/KWREUT": "{^git init}"                                                                                                   # GIT InIT
"TKPWEUT/P*UL": "{^git pull --rebase}"                                                                                            # GIT PULL (rebase)
"TKPWEUT/P*UL/O*RPBLG/PHAEUPB": "{^git pull --rebase origin main}"                                                                # GIT PULL (rebase) ORIGIN MAIN
"TKPWEUT/P*UL/O*RPBLG/PHAFRT": "{^git pull --rebase origin master}"                                                               # GIT PULL (rebase) ORIGIN MASTER
"TKPWEUT/P*UL/O*RPBLG/PWRAFRPB": "{^git pull --rebase origin $(git symbolic-ref HEAD --short)}"                                   # GIT PULL (rebase) ORIGIN (current BRANCH name)
"TKPWEUT/P*UL/STPRAOEPL/PHAEUPB": "{^git pull --rebase upstream main}"                                                            # GIT PULL (rebase) uPSTREAM MAIN
"TKPWEUT/P*UL/STPRAOEPL/PHAFRT": "{^git pull --rebase upstream master}"                                                           # GIT PULL (rebase) uPSTREAM MASTER
"TKPWEUT/P*UL/STPRAOEPL/PWRAFRPB": "{^git pull --rebase upstream $(git symbolic-ref HEAD --short)}"                               # GIT PULL (rebase) uPSTREAM (current BRANCH name)
"TKPWEUT/P*URB": "{^git push --force}"                                                                                            # GIT PUSH (force)
"TKPWEUT/P*URB/O*RPBLG/PWRAFRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUT/PHERPBLG/STPRAOEPL/PHAEUPB": "{^git merge upstream/main}"                                                                # GIT MERGE uPSTREAM MAIN
"TKPWEUT/PHERPBLG/STPRAOEPL/PHAFRT": "{^git merge upstream/master}"                                                               # GIT MERGE uPSTREAM MASTER
"TKPWEUT/PUL": "{^git pull}"                                                                                                      # GIT PULL
"TKPWEUT/PUL/O*RPBLG/PHAEUPB": "{^git pull origin main}"                                                                          # GIT PULL ORIGIN MAIN
"TKPWEUT/PUL/O*RPBLG/PHAFRT": "{^git pull origin master}"                                                                         # GIT PULL ORIGIN MASTER
"TKPWEUT/PUL/O*RPBLG/PWRAFRPB": "{^git pull origin $(git symbolic-ref HEAD --short)}"                                             # GIT PULL ORIGIN (current BRANCH name)
"TKPWEUT/PUL/STPRAOEPL/PHAEUPB": "{^git pull upstream main}"                                                                      # GIT PULL uPSTREAM MAIN
"TKPWEUT/PUL/STPRAOEPL/PHAFRT": "{^git pull upstream master}"                                                                     # GIT PULL uPSTREAM MASTER
"TKPWEUT/PUL/STPRAOEPL/PWRAFRPB": "{^git pull upstream $(git symbolic-ref HEAD --short)}"                                         # GIT PULL uPSTREAM (current BRANCH name)
"TKPWEUT/PURB": "{^git push}"                                                                                                     # GIT PUSH
"TKPWEUT/PURB/O*RPBLG/PWRA*FRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUT/PURB/O*RPBLG/PWRAFRPB": "{^git push origin $(git symbolic-ref HEAD --short)}"                                            # GIT PUSH ORIGIN (current BRANCH name)
"TKPWEUT/PWHRA*EUPL": "{^git blame -wM}"                                                                                          # GIT BLAME (-w ignore whitespace, -M find line movements)
"TKPWEUT/PWRA*FRPB": "{^git branch --verbose}"                                                                                    # GIT BRANCH (verbose)
"TKPWEUT/PWRAFRPB/SROEBS": "{^git branch --verbose}"                                                                              # GIT BRANCH VERBOSE
"TKPWEUT/R*PL": "{^git rm --force}"                                                                                               # GIT RM (force)
"TKPWEUT/R-PL": "{^git rm}"                                                                                                       # GIT RM
"TKPWEUT/RAOEBS": "{^git rebase}"                                                                                                 # GIT REBase
"TKPWEUT/RAOEBS/PWORT": "{^git rebase --abort}"                                                                                   # GIT REBase ABORT
"TKPWEUT/RAOEBS/T-PB": "{^git rebase --continue}"                                                                                 # GIT REBase CONTINUE
"TKPWEUT/RAOEBS/TPHRAF": "{^git rebase --interactive}"                                                                            # GIT REBase INTERACTIVE
"TKPWEUT/RAOEPLT": "{^git remote --verbose}"                                                                                      # GIT REMOTE verbose
"TKPWEUT/ST*TS": "{^git status}"                                                                                                  # GIT STATUS
"TKPWEUT/ST-TS": "{^git status --short}"                                                                                          # GIT STATUS (short)
"TKPWEUT/STARB": "{^git stash}"                                                                                                   # GIT STASH
"TKPWEUT/STARB/POP": "{^git stash pop}"                                                                                           # GIT STASH POP
"TKPWEUT/STARB/PURB": "{^git stash push}"                                                                                         # GIT STASH PUSH
"TKPWEUT/TK*EUF": "{^git diff --ignore-all-space}"                                                                                # GIT DIFF (ignore all space)
"TKPWEUT/TKEUF": "{^git diff}"                                                                                                    # GIT DIFF
"TKPWEUT/TKPEUG/HR*EUS": "{^git config --list}"                                                                                   # GIT CONFIG LIST
"TKPWEUT/TPH*EUT": "{^git init}"                                                                                                  # GIT iNIT
"TKPWEUTD": "{^git add}"                                                                                                          # GIT aDD
"TKPWO*P": "{^git stash pop}"                                                                                                     # Git stash pOP
"TKPWOP": "{^git stash pop}"                                                                                                      # Git stash pOP
```

## [gh](https://cli.github.com/)

```yaml
TKPWH: gh
```

## [commitizen](https://commitizen-tools.github.io/commitizen/)

```yaml
KR*Z : cz
KR*Z/KR*Z : cz bump
```

## [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)

Powershell module CrossPlatformDotFiles repository function helpers to help
build the commit message.

```yaml
TKPWEUPLT : git commit --message=\"$(Select-ConventionalCommitValue){^}
TKPWEUPLTD : git commit --all --message=\"$(Select-ConventionalCommitValue){^}
SKO*EPD: {^}($(Select-ConventionalCommitFileScope)):{^ ^}
```

```yaml
SR*EPBL: fix
SR*EPBL/SR*EPBL: feat
SR*EPBL/SR*EPBL/SR*EPBL: build
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: chore
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: ci
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: docs
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: style
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: refactor
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: perf
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: test
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: feat
SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL/SR*EPBL: feat
```

## [pre-commit](https://pre-commit.com/)

```yaml
PRE/KPHEUT : pre-commit
PREUPLT : pre-commit # overwrites perimeter
```
