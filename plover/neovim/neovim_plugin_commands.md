# Neovim Plugin Commands

This dictionary is meant to be exclusively for neovim plugin commands and
mappings. I will organize it similar to how I have it mapped in my neovim
configuration, and that is by [which-key](https://github.com/folke/which-key.nvim)
groupings.

which-key is a plugin that helps you remember your mappings. I use `,` as my
neovim leader key and so most of these commands start with `,`.

## Leader + `d` 🟰 **debug**

## G Commands

Any command that starts with `g` or `G` or `:g`.
There are so many they deserve their own category.

See [neovim_core_commands](./neovim_core_commands.md#G Commands)
for similar mappings for neovim core commands like `gg`.

```yaml
K-PL           :  {^gcc^} # Comment current line in line wise style
K-PLT          :  {^gcip^} # Comment current block in a line wise style
K*PL           :  {^gbc^} # Comment current line in block wise style
```

## Personal Mappings That Need To Be Fast

```yaml
KH*EBGD            :  {^},vl{^} # Mark down check box
TRAO*E             :  {^},fe{^} # File tree toggle
TRAO*ES            :  {^},ft{^} # Telescope file browser
T*EFT              :  {^},ui{^} # Test
R*UPB              :  {^},uu{^} # Run
PW-D               :  {^},u;{^} # Build
KW*EUBG            :  {^},la{^} # LSP code action version 1
KWO*EUBG            :  {^},lb{^} # LSP code action version 2
TKPW*URB           :  {^}Pp{^} # Git push (gush)
TPO*RPLT           :  {^},lf{^} # Format code
TKPW*URB/TKPW*URB  :  {^}git push\\n
TKPW*UL            :  {^}pp{^} # Git pull (gull)
TKPW*UL/TKPW*UL    :  {^}git pull\\n
PHRA*US            :  {^}vip:s/{^}   # 'plahs' for selecting paragraph and start replace
HRA*US             :  {^}gv:s/{^}    # 'lahs' for selecting previous selection and start replace
TPAO*EUL           :  {^},fF{^} # File search
TKPWAO*EUL         :  {^},fG{^} # (Guiles) File search for git files
PW*UFR             :  {^},fb{^} # Search buffers
TKPWR*EP           :  {^},fg{^} # Grep files command
TKPWR*EPS          :  {^},fs{^} # Grep string under cursor
HOEUP              :  {^},fh{^} # Grep files command
TK*EUFR            :  {^},gd{^} # Call plugin DiffViewOpen
TKPW*EUT           :  {^},g1{^} # Call primary git plugin in neovim
TKPWO*EUT           :  {^},g2{^} # Call next git plugin in neovim
TKPWA*EUT           :  {^},g3{^} # Call next git plugin in neovim
HRA*EZ             :  {^},aa{^} # Lazy (package manager)
TR*EUT         :  {^},ab{^} # :TSPlaygroundToggle<CR>')
HRO*EDZ         :  {^},ac{^} # Reload my entire neovim config
TPHO*ET         :  {^},ad{^} # Show recent notifications
PHR*EPB       : {^},dP{^} # Run plenary tests for neovim plugins
WRAO          : {^}]d{^} # Forward to next diagnostic
KWAO          : {^}[d{^} # Backward to previous diagnostic
SKO*EP        : {^},ff{^} # Open telescope general prompt
TP*UZ        : {^},fz{^} # Open telescope fuzzy find current buffer
KPHA*PBD      : {^},fc{^} # Telescope open command history
TA*EUP : {^},nt{^} # Toggle tapey-tape-plugin
TR*EUPL : {^},mt{^} # MiniTrailspace.trim()
TR*EUPLS : {^},mT{^} # MiniTrailspace.trim.last_lines()
TKPW*EUTS : {^},fS{^} # Telescope git status search
SR*EUPL : {^},fv{^} # Telescope nvim config directory
SR*EUPLS : {^},fV{^} # Telescope live grep nvim config directory
PHRO*F : {^},fp{^} # Telescope Plover dictionary directory
PHRO*FS : {^},fP{^} # Telescope live grep Plover dictionary directory
P-PL : {^},gj{^}
P-FP : {^},gk{^}
HRAO*EUPBS : {^},ll{^} # LSPlines plugin toggle
TKPWUGT : {^}g?p{^} # Debug print plugin current line
TKPWUGS : {^}g?v{^} # Debug print plugin current variable
```

## Treesitter Mappings

```yaml
T-PL : {^},tnfs{^}
T-FP : {^},tpfs{^}
T*PL : {^},tnfe{^}
T*FP : {^},tpfe{^}
```
