import time
import random

print('-' * 65)
print('Magic Eight Ball')
print()

question = input('What is your question ')
print('Shaking!')
time.sleep(1)
print('...thinking...')
time.sleep(1)
print('...thinking...')
time.sleep(1)

choice = random.randint(1,4)

if choice == 1:
	print('Yes, do it!')
elif choice == 2:
	print('No!!!!')
elif choice == 3:
	print('Maybe you should not ask a ball to think for you.')
elif choice == 4:
	print('The choice is up to you.')
elif choice == 5:
	print('Try asking again.')
else:
	print('No!!!')