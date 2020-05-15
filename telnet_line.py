import telnetlib

host = "103.60.17.100"
port = 5787
timeout = 100

with telnetlib.Telnet(host, port, timeout) as session:
    while True:
        line = session.read_until(b"\n")  # Read one line

        if b'Wow' in line:  # last line, no more read
            line = session.read_until(b"!!!end!!!\r\n")
            print(line)
            break

        a = line.decode("utf-8").strip().split()
        b = int(a[-3])
        c = int(a[-1])
        result = (str(b + c) + "\n").encode("utf-8")

        session.write(result)
        line = session.read_until(b"\n") # skip a line
