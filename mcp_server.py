import sys
import json
from client import ConvolutionalViterbi

def main():
    conv = ConvolutionalViterbi()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "encode":
            e = conv.encode(params.get("bits", []))
            res = {"encoded": e}
        elif method == "decode":
            d = conv.decode(params.get("received", []))
            res = {"decoded": d}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
