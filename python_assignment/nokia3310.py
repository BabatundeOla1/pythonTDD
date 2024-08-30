main_menu = """ 	   Main menu 
-------------------------
1 -> Phone book
2 -> Message
3 -> Chat
4 -> Call Register
5 -> Tones
6 -> Settings 
7 -> Call Diverting 
8 -> Games
9 -> Calculator
10 -> Reminders
11 -> Clock
12 -> Profile 
13 -> SIM Service
-------------------------
	Enter a number:
"""

menu = input(main_menu)

match menu: 

	case'1': 
		print("Phone Book\n")

		phone_book = input("1: Search\n2: Service No\n3: Add name\n4: Erase\n5: Edit\n6: Assign tone\n7: Send b'card\n8: Options\n9: Speed dial\n10: Voice tags\n")

		match phone_book:

			case'1':
				print("Search")

			case'2': 
				print("Service")

			case'3':
				print("Add name")

			case'4': 
				print("Erase")

			case'5':
				print("Edit")

			case'6': 
				print("Assign tone")

			case'7':
				print("Send b'card")

			case'8': 
				print("Options")
				options = input("1: Search book\n2: Service NOs")

				match options: 

					case'1': 
						print("Search book")

					case'2': 
						print("Service NOs")

			case'9':
				print("Speed dial")

			case'10':
				print("Voice tags")

	case'2': 
		print("Message\n")

		Message = input("1: Write message\n2: Inbox\n3: Outbox\n4: Picture message\n5: Templates\n6: Smileys\n7: Message settings\n8: Info service\n9: Voice mailbox number\n10: Service command Operator\n")
				
		match Message: 

			case'1':
				print("Write message")

			case'2': 
				print("Inbox")

			case'3':
				print("Outbox")

			case'4': 
				print("Picture message")

			case'5':
				print("Templates")

			case'6': 
				print("Smileys")

			case'7':
				print("Message setting")
				message_settings = input("1: Set 1\n2: Common")

				match message_settings: 

					case'1': 
						print("Set")
						set = input("1: Message centre number\n2: Message sent as\n3: Message validity")
						
						match set:
			
							case'1':
								print("Message centre number")

							case'2': 
								print("Message sent as")

							case'3': 
								print("Message validity")

					case'2': 
						print("Common")
						common = input("1: Delivery reports\n2: Reply via same centre\n3: Character support")
				
						match common:

							case'1': 
								print("Delivery reports")

							case'2': 
								print("Reply via same centre")

							case'3': 
								print("Character suppor")

			case'8': 
				print("Info service")
			
			case'9':
				print("Voice mailbox number")

			case'10': 
				print("Service command operator")
				






