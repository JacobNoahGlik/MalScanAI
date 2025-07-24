# Run this inside Ghidra's Script Manager to start GhidraBridge
from ghidra.app.script import GhidraScript

class ConnectBridge(GhidraScript):
    def run(self):
        import sys
        sys.path.append("/path/to/ghidra_bridge")  # Update path
        import ghidra_bridge
        ghidra_bridge.GhidraBridge(namespace=globals())
