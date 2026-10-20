# Add the dynamic simulation script
git add dynamic_horizon_simulation.py

# Mark as executable in git index
git update-index --chmod=+x dynamic_horizon_simulation.py

# Commit and push changes
git commit -m "feat: add dynamic_horizon_simulation.py modeling time-evolved constraint boundaries"
git push origin main
