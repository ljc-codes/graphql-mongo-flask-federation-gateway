
echo '# Stage 1: Purge Current Build (shell)'
./scripts/purge_build.sh

echo '# Stage 2: Compiling New Build (shell)'
./scripts/compile_build.sh

echo '# Stage 3: Dockerizing Build (docker)'
./scripts/dock_build.sh