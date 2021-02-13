import csv
import os #para limpiar la consola con cada ejecución
import re #para validar input de mail

class Contact:

    def __init__(self, name,dni,phone,email):
        self.name = name
        self.dni = dni
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    #def load_contacts(self,name,dni,phone,email):
    #    contact = Contact(name,dni,phone,email)
    #    self._contacts.append(contact)

    def add(self,name,dni,phone,email):
        contact = Contact(name,dni,phone,email)
        self._contacts.append(contact)
        self._save()

    def modify(self,contact_modify,var_modify):
        for contact in self._contacts:
            if contact.dni.lower() == contact_modify.lower():
                self._print_contact(contact)
                print('This Contact is will modify {}  '.format(var_modify))
                print('')
                date_modify = str(input('Add New {}  '.format(var_modify)))
                print('')

                if var_modify == 'name':
                    contact.name = date_modify
                    print('')
                    print('')
                    print('This Contact Modify:')
                    self._print_contact(contact)
                    self._save()

                if var_modify == 'dni':
                    contact.dni = date_modify
                    print('')
                    print('')
                    print('This Contact Modify:')
                    self._print_contact(contact)
                    self._save()

                if var_modify == 'phone':
                    contact.phone = date_modify
                    print('')
                    print('')
                    print('This Contact Modify:')
                    self._print_contact(contact)
                    self._save()

                if var_modify == 'email':
                    contact.email = date_modify
                    print('')
                    print('')
                    print('This Contact Modify:')
                    self._print_contact(contact)
                    self._save()
                                


    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def search_dni(self, dni):
        for contact in self._contacts:
            if contact.dni.lower() == dni.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()   

    def search_name(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _print_contact(self, contact):
        print('----------------------------------------------')
        print('Name: {}'.format(contact.name))
        print('DNI: {}'.format(contact.dni))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('----------------------------------------------')

        
    def _save(self):
        with open('contacts.csv', 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name','dni','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name,contact.dni,contact.phone,contact.email))

    def delete(self, dni):
        for idx, contact in enumerate(self._contacts):
            if contact.dni.lower() == dni.lower():
                while True:               
                    self._print_contact(contact)
                    delete_decision = input('''
                            You are sure delete this contact..?     
                            
                            [Y]es
                            [N]o

                            ''')

                    if delete_decision == 'Y':
                        del self._contacts[idx]
                        self._save()
                        break 
                    else:
                        break                      
             
             
def run():

    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex_dni = '^[0-9]{6,8}$'  
    regex_phone = '^[0-9]{2}-[0-9]{8}$'

    contact_book = ContactBook()
    
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in list(enumerate(reader)):
            if idx == 0:
                continue

            contact_book.add(row[0],row[1],row[2],row[3])
    

    while True:
        command = str(input('''
            What Do you want do?

            [a]dd contact
            [m]odify contact
            [s]earch contact
            [d]elete contact
            [l]ist contact
            [e]xit
        
        '''))
        print('')
        print('')

        if command == 'a':
           
            print('')
            name = str(input('Add Name:  ')) #***********************  NAME  **********************
            
            while True:
                dni = str(input('Add DNI number:  ')) #*******************   DNI  *********************************                          
                if(re.search(regex_dni,dni)):  
                    break  
                else:
                    print('')  
                    print("Invalid DNI, try again")
                    print('') 

            while True:
                phone = str(input('Add Phone number:  ')) #******************** Phone *******************************
                if(re.search(regex_phone,phone)):  
                    break  
                else:
                    print('')  
                    print("Invalid Phone, try again")
                    print('')                     
            
            while True:
                email = str(input('Add email:  '))  #********************** email  ********************************
                if(re.search(regex_email,email)):  
                    break  
                else:
                    print('')  
                    print("Invalid Email, try again")
                    print('')

            print('')
            print('Please, verify the information.')
            print('''
            Name:{}
            DNI: {}
            Phone: {}
            Email: {}          
            '''.format(name,dni,phone,email))
            print('')
            
            while True:
                verify_info = str(input('''
            ¿Is it correct?

            [Y]es
            [N]o
            
            '''))

                if verify_info == 'Y':
                    contact_book.add(name,dni,phone,email)
                    break
                elif verify_info == 'N':
                    print('Try again add all information')
                    break                    
                else:
                    print('This command not exit, try again')         
                                    
        elif command == 'm':  #**************************************** MODIFY ************************************
            
            contact_modify = str(input('Add DNI to contact modify: '))
            var_modify = str(input('''
                What data do you want modify..?

                [name]
                [dni
                [phone]
                [email]   
                   
            '''))

            A = ['name','dni','phone','email']

            if var_modify.lower() in A:
                contact_book.modify(contact_modify,var_modify)
                    
            else:
                print('This command not exit, try again') 
                continue
                        
                      
            
        elif command == 's': #**************************************** SEARCH ************************************ 
            methode_search = input(str('''
            How do you want search contact? by..
            
            [D]NI
            [N]ame
            
            '''))

            if methode_search == 'D':
                dni = str(input('Add DNI to search: '))
                contact_book.search_dni(dni)
            elif methode_search == 'N':
                name = str(input('Add Name to search: '))
                contact_book.search_name(name)
            else:
                print('This command not exit, try again')

          
        elif command == 'd': #********************************** DELETE ******************************************
            name = str(input('Add DNI to search to Delete: '))

            contact_book.delete(name)                     

            
        elif command == 'l': #************************************* LIST ******************************************

            contact_book.show_all()
            
        elif command == 'e':
            print('Good Bye!!')
            break
        else:
            print('This command not exit, try again')
            
if __name__ == '__main__':
    print('')
    print('Welcome to Your Contact Book')
    print('')

    run()