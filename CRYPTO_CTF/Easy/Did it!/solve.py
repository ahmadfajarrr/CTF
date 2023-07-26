from pwn import *

def find_K():
    host = '01.cr.yp.toc.tf'
    port = 11337
    r = remote(host, port)

    # Receive initial messages from the server
    r.recvline()
    r.recvline()
    r.recvline()

    n, l = 127, 20
    dic = {}
    for i in range(n):
        dic[i] = pow(i, 2, n)

    list_of_inputs = []
    added_to_list = [False] * n

    # Generate subsets that satisfy certain conditions and add them to the list_of_inputs
    while added_to_list != [True] * n:
        input = []
        collision_check = set()
        count = 0
        for i in range(127):
            if added_to_list[i] == True:
                continue
            if dic[i] - 1 not in collision_check and dic[i] not in collision_check and dic[i] + 1 not in collision_check:
                input.append(i)
                collision_check.add(dic[i])
                collision_check.add(dic[i] + 1)
                added_to_list[i] = True
                count += 1
            if count == 20:
                break
        list_of_inputs.append(input)

    K = []

    # Iterate through the subsets in the list_of_inputs
    for i in range(len(list_of_inputs)):
        s = ','.join(map(str, list_of_inputs[i]))
        r.sendline(s.encode())
        did = r.recvline().decode().strip()
        not_in_k = did.lstrip('+ DID = [').rstrip(']')
        lis = list(map(int, not_in_k.split(', ')))

        # Check the response from the server and find elements not in K
        for num in list_of_inputs[i]:
            if dic[num] not in lis and dic[num] + 1 not in lis:
                K.append(num)

    s = ','.join(map(str, K))
    r.sendline(s.encode())

    # Get the final result from the server and return it
    r.recvline()
    result = r.recvline().decode().strip()

    # Close the connection
    r.close()

    return result

if __name__ == "__main__":
    result = find_K()
    print(result)
