def decode_cassette_tape():
    filename = input("Enter the cassette tape file path: ")

    try:
        with open(filename, 'rb') as file:
            num_blocks = int.from_bytes(file.read(2), byteorder='little')
            print(f"Number of blocks: {num_blocks}")

            for block_num in range(num_blocks):
                block_type = int.from_bytes(file.read(1), byteorder='little')
                block_length = int.from_bytes(file.read(3), byteorder='little')
                data = file.read(block_length)

                print(f"\nBlock {block_num + 1}:")
                print(f"Type: {block_type}")
                print(f"Length: {block_length} bytes")

                if block_type == 0x00:
                    print(f"Data: {data.decode('ascii')}")
                elif block_type == 0x01:
                    print("End of Tape Block")
                elif block_type == 0x02:
                    print("Archive Block")
                elif block_type == 0x03:
                    print("Program Block")
                else:
                    print("Unknown Block Type")

    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")


decode_cassette_tape()
