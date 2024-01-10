import asyncio
async def control():
    r=1
    while r==True:
        try:
            start = int(input("Enter start value for start: "))
            end = 0
            for i in range(start, end - 1, -1):
                await asyncio.sleep(1)
                print(i)
            r=False
        except ValueError:
            print("Enter number")
async def main():
    result_control = await control()
    print(result_control)

if __name__ == "__main__":
    asyncio.run(main())