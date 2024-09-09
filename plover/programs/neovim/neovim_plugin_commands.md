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
K-PL: "{^gcc^}" # Comment current line in line wise style
K-PLT: "{^gcip^}" # Comment current block in a line wise style
K*PL: "{^gbc^}" # Comment current line in block wise style
```

I've mapped more of the comment commands this plugin can do using the Emily's
symbols python file. These are the mappings (note that it is a python code
block, the markdown dictionary plugin only works with an empty syntax or yaml)

```python
# Commands for use with comment-nvim for easy line comments
# Using the directal inputs you can easily start I comment at eol,
# above, or below
"RLG": ["gcO", "", "gcA", "gco"],
```

## My Plugins

```yaml
TOG: "{^,nB^}" # Boolean toggle
```

## Personal mappings That Need To Be Ultra Fast

Often useds in my .nvim.lua project files

### Running

```yaml
R-B                :  {^}`r1{^} # Run action 1
R-G                :  {^}`r2{^} # Run action 2
R-S                :  {^}`r3{^} # Run action 3
```

### Building

```yaml
R-P               :  {^}`b1{^} # Build action 1
R-L               :  {^}`b2{^} # Build action 2
R-T               :  {^}`b3{^} # Build action 3
```

### Testing

```yaml
T*EFT              :  {^}`ui{^} # Test, note the ` instead of , this keeps it more usable in insert mode without delays
T-FT               :  {^}`ui{^} # Test shorter alternative
```

## Personal Mappings That Need To Be Fast

```yaml
KH*EBGD            :  {^},vl{^} # Mark down check box
TRAO*E             :  {^},fe{^} # File tree toggle
TRAO*ES            :  {^},ft{^} # Telescope file browser
KW*EUBG            :  {^},la{^} # LSP code action version 1
KWO*EUBG           :  {^},lb{^} # LSP code action version 2
TPO*RPLT           :  {^},lf{^} # Format code
PHRA*US            :  {^}vip:s/{^}   # 'plahs' for selecting paragraph and start replace
HRA*US             :  {^}gv:s/{^}    # 'lahs' for selecting previous selection and start replace
TPAO*EUL           :  {^},fF{^} # File search
TKPWAO*EUL         :  {^},fG{^} # (Guiles) File search for git files
PW*UFR             :  {^},fb{^} # Search buffers
TKPWR*EP           :  {^},fg{^} # Grep files command
TKPWR*EPS          :  {^},fs{^} # Grep string under cursor
HOEUP              :  {^},fh{^} # Grep files command
HRA*EZ             :  {^},aa{^} # Lazy (package manager)
HRO*EDZ         :  {^},ac{^} # Reload my entire neovim config
TPHO*ET         :  {^},ad{^} # Show recent notifications
PHR*EPB       : {^},dP{^} # Run plenary tests for neovim plugins
WRAO          : {^}]d{^} # Forward to next diagnostic
KWAO          : {^}[d{^} # Backward to previous diagnostic
SKO*EP        : {^},ff{^} # Open telescope general prompt
TP*UZ        : {^},fz{^} # Open telescope fuzzy find current buffer
KPHA*PBD      : {^},fc{^} # Telescope open command history
TA*EUP : {^},nt{^} # Toggle tapey-tape-plugin
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

## [nvim-Treesitter](https://github.com/nvim-treesitter/nvim-treesitter)

[Treesitter](https://github.com/tree-sitter/tree-sitter) is a incremental text parser library.

```yaml
TREUT  : treesitter # Amazing smart parsing tool
TR*EUT : {^},ab{^} # Open a live tree view of the current file, test queries, etc.
T-PL   : {^},tnfs{^}
T-FP   : {^},tpfs{^}
T*PL   : {^},tnfe{^}
T*FP   : {^},tpfe{^}
```

## [Luasnip](https://github.com/L3MON4D3/LuaSnip)

Ultra powerful snippet plugin written in lua by

```yaml
HROEUP: luasnip
HR*EUP: luasnip
HRAOU/STPHEUP: luasnip
```

## Mini.nvim

```yaml
TR*EUPL             : {^},mt{^}         # MiniTrailspace.trim()
TR*EUPLS            : {^},mT{^}         # MiniTrailspace.trim.last_lines()
TPO*RPLTD           : {^}gaip:{^}       # MiniTrailspace.trim.last_lines()
TPO*RPLTD/TPO*RPLTD : {^}gaip:gaip\#{^} # MiniTrailspace.trim.last_lines()
```

## Git Plugins

### All

```yaml
TKPW*URB           :  {^},gP{^} # Git push (gush)
TKPW*URB/TKPW*URB  :  {^}git push\\n
TKPW*UL            :  {^},gp{^} # Git pull (gull)
TKPW*UL/TKPW*UL    :  {^}git pull\\n
TKPW*EUT           :  {^},g1{^} # Call primary git plugin in neovim
TKPWO*EUT           :  {^},g2{^} # Call next git plugin in neovim
TKPWA*EUT           :  {^},g3{^} # Call next git plugin in neovim
```

### DiffView.nvim

```yaml
TK*EUF            :  {^},gd{^} # Call my special function to toggle diff view
TK*EUFR           :  {^}{\#Escape}:DiffviewFileHistory %{^} # Diff file history for currently opened file
TK*EUFPL          :  {^}{\#Escape}:DiffviewOpen{^ ^} # Better starter for diff view open
TK*EUFPLT         :  {^}{\#Escape}:DiffviewClose \\n
```

### [Luapad](https://github.com/rafcamlet/nvim-luapad)

This plugin has helped me so much with building skill with both lua and name
configuration. It works as an inline repl, showing the code results as virtual
text.

```yaml
HRAOUPD : {^},dV{^} # LuaPaD: used to run some of my saved files in my neovim configuration that I call the "playground", where I test neovim APIs
HRAO*UPD : {^}{\#Escape}:Luapad\\n{^} # Open luapad in scratch buffer with realtime evaluation
```

### dadbod.vim

```yaml
PWO*D : {^}{\#Escape}:DBUIToggle\\n{^}
```

### [Harpoon](Harpoon)

```yaml
-FPL   : {^}{\#Escape},ha{^} # Add to harpoon
*L     : {^}{\#Escape},hb{^} # Next harpoon item
*F     : {^}{\#Escape},hc{^} # Previous harpoon item
*P     : {^}{\#Escape},hp{^} # Pick harpoon item
*FPL   : {^}{\#Escape},hP{^} # Pick harpoon item (editable)
*R     : {^}{\#Escape},h1{^} # Go to harpoon item 1 (similar binary number picker to Emily's modifiers)
*B     : {^}{\#Escape},h2{^} # Go to harpoon item 2
*RB    : {^}{\#Escape},h3{^} # Go to harpoon item 3
*G     : {^}{\#Escape},h4{^} # Go to harpoon item 4
*RG    : {^}{\#Escape},h5{^} # Go to harpoon item 5
*BG    : {^}{\#Escape},h6{^} # Go to harpoon item 6
*RBG   : {^}{\#Escape},h7{^} # Go to harpoon item 7
*S     : {^}{\#Escape},h8{^} # Go to harpoon item 8
*RS    : {^}{\#Escape},h9{^} # Go to harpoon item 9
*BS    : {^}{\#Escape},hA{^} # Go to harpoon item A
*RBS   : {^}{\#Escape},hA{^} # Go to harpoon item B
*GS    : {^}{\#Escape},hA{^} # Go to harpoon item C
*RGS   : {^}{\#Escape},hA{^} # Go to harpoon item D
*BGS   : {^}{\#Escape},hA{^} # Go to harpoon item E
*RBGS  : {^}{\#Escape},hA{^} # Go to harpoon item F
```

### Pairs Plugins

I used to use vim unimpaired by TPope, but now I use Mini.Pairs.
And there are some mappings that are built into neovim such as
`]c` for jumping to the next diff and I want to include any such maps here as
well.

```yaml
#AFS      : {^]a^}
#A*FS     : {^[a^}
#PWFS     : {^]b^}
#PW*FS    : {^[b^}
#KRFS     : {^]c^}
#KR*FS    : {^[c^}
#TK-FS    : {^]d^}
#TK*FS    : {^[d^}
#-EFS     : {^]e^}
#*EFS     : {^[e^}
#TP-FS    : {^]f^}
#TP*FS    : {^[f^}
#H-FS     : {^]h^}
#H*FS     : {^[h^}
#-EUFS    : {^]i^}
#*EUFS    : {^[i^}
#SKWRFS   : {^]j^}
#SKWR*FS  : {^[j^}
#K-FS     : {^]k^}
#K*FS     : {^[k^}
#HR-FS    : {^]l^}
#HR*FS    : {^[l^}
#PH-FS    : {^]m^}
#PH*FS    : {^[m^}
#TPH-FS   : {^]n^}
#TPH*FS   : {^[n^}
#O-FS     : {^]o^}
#O*FS     : {^[o^}
#P-FS     : {^]p^}
#P*FS     : {^[p^}
#KW-FS    : {^]q^}
#KW*FS    : {^[q^}
#R-FS     : {^]r^}
#R*FS     : {^[r^}
#S-FS     : {^]s^}
#S*FS     : {^[s^}
#T-FS     : {^]t^}
#T*FS     : {^[t^}
#-UFS     : {^]u^}
#*UFS     : {^[u^}
#SR-FS    : {^]v^}
#SR*FS    : {^[v^}
#W-FS     : {^]w^}
#W*FS     : {^[w^}
#KP-FS    : {^]x^}
#KP*FS    : {^[x^}
#KWR-FS   : {^]y^}
#KWR*FS   : {^[y^}
#STKPW-FS : {^]z^}
#STKPW*FS : {^[z^}
```
