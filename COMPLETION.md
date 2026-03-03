# ⚛️ SPIMAG Shell Completion

SPIMAG provides shell completion for bash, zsh, and fish shells.

---

## Installation

### Bash
```bash
eval "$(_SPIMAG_COMPLETE=bash_source spimag)"
```

Zsh

```zsh
eval "$(_SPIMAG_COMPLETE=zsh_source spimag)"
```

Fish

```fish
eval (env _SPIMAG_COMPLETE=fish_source spimag)
```

---

Available Commands

Core Commands

Command Description
spimag analyze Run SMNI analysis
spimag monitor Monitor spin coherence
spimag dashboard Launch dashboard
spimag species List migratory species
spimag alerts Check geomagnetic alerts

Parameter Commands

```bash
spimag analyze s-yield        # Spin Quantum Yield
spimag analyze dE-zeeman      # Zeeman Energy Splitting
spimag analyze gamma-coh       # Quantum Coherence Lifetime
spimag analyze theta-inc       # Magnetic Inclination Sensitivity
spimag analyze chi-para        # Paramagnetic Susceptibility
spimag analyze p-singlet       # Singlet-Triplet Probability
spimag analyze omega-dipole    # Dipolar Coupling Tensor
spimag analyze v-nav           # Navigational Vector Precision
spimag analyze smni            # Composite Score
```

Species Commands

```bash
spimag species list                         # List all 31 species
spimag species show --id erithacus-rubecula # Show species details
spimag species compare --sp1 a --sp2 b      # Compare two species
spimag species family --type passerine       # Filter by family
```

Alert Levels

```bash
spimag alerts --status watch      # SMNI 0.55-0.72
spimag alerts --status alert      # SMNI 0.38-0.55
spimag alerts --status emergency  # SMNI 0.30-0.38
spimag alerts --status critical   # SMNI < 0.30
```

Geomagnetic Storm Monitoring

```bash
spimag storm status               # Current geomagnetic storm status
spimag storm map --region global  # Show storm impact map
spimag storm predict --hours 24   # Predict SMNI disruption
```

---

Examples

```bash
# Analyze European Robin cryptochrome
spimag analyze --species erithacus-rubecula --parameters all

# Monitor coherence lifetime
spimag monitor gamma-coh --species erithacus-rubecula --duration 72h

# Check active alerts during geomagnetic storm
spimag alerts --status alert --region europe

# List all species with quantum coherence >5 µs
spimag species list --coherence-min 5.0 --details

# Calculate SMNI for specific dataset
spimag smni --dataset cry4a-2026-001 --verbose

# Run hypothesis test (H1-H8)
spimag test --hypothesis H1 --verbose

# Launch dashboard
spimag dashboard --port 8501

# Simulate spin dynamics
spimag simulate --field 50 --inclination 45 --coherence 6.2
```

---

Tab Completion Features

Species Name Completion

· Auto-completes from 31 migratory species
· Groups by taxonomic family

Parameter Completion

· All 8 SMNI parameters
· Parameter groups (quantum, behavioral, environmental)

Family/Order Completion

· passeriformes (songbirds)
· lepidoptera (butterflies)
· testudines (turtles)
· columbiformes (pigeons)
· salmoniformes (fish)

Region Completion

· europe
· north-america
· south-america
· africa
· asia
· australia

Alert Status Colors

· 🟢 WATCH     (SMNI 0.55-0.72)
· 🟡 ALERT     (SMNI 0.38-0.55)
· 🟠 EMERGENCY (SMNI 0.30-0.38)
· 🔴 CRITICAL  (SMNI < 0.30)

---

Environment Variables

```bash
export SPIMAG_CONFIG=~/.spimag/config.yaml
export SPIMAG_DATA_DIR=/data/spimag
export SPIMAG_NOAA_API_KEY=your_key_here
export SPIMAG_INTERMAGNET_TOKEN=your_token_here
```

---

Live Resources

· Dashboard: https://spimag.netlify.app
· Documentation: https://spimag.readthedocs.io
· NOAA Space Weather: https://swpc.noaa.gov
· INTERMAGNET: https://intermagnet.org

---

⚛️ Inside the eye of a migrating robin, two electrons are entangled. SPIMAG decodes.
