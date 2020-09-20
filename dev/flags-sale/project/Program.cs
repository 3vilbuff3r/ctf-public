using System;

namespace FlagShop
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Flags shop!");
            int balance = 1000;
            int cost = 1337;
            int cost_dummy = 100;
            Console.WriteLine($"The bank gives you {balance} cash to shop around.");
            while (true)
            {
                Console.WriteLine("Menu:\n1. Check balance\n2. Buy Flag\n3. Exit");
                int choice;
                if(int.TryParse(Console.ReadLine(), out choice))
                {
                    if(choice == 1)
                    {
                        Console.WriteLine($"Balance is {balance}");
                        continue;
                    } 
                    else if (choice == 2)
                    {
                        Console.WriteLine($"Available Flags Menu: \n1. Dummy flag: For {cost_dummy}\n2. Elite flag: For {cost}\nWhich one do you want??");
                        int flag_choice;
                        if (int.TryParse(Console.ReadLine(), out flag_choice))
                        {
                            if (flag_choice == 2)
                            {
                                Console.WriteLine($"Enter quantity:");
                                int quantity;
                                if (int.TryParse(Console.ReadLine(), out quantity))
                                {
                                    if(quantity > 0 && quantity * cost <= balance)
                                    {
                                        balance -= (quantity * cost);
                                        Console.WriteLine("Here's the flag: m365{int3g3r_0verfl0w}");
                                    }
                                    else
                                    {
                                        Console.WriteLine("Insufficient funds. Looks like we have similar bank accounts.");
                                    }
                                }
                                else
                                {
                                    Console.WriteLine("Not int. Try again.");
                                    continue;
                                }
                            }
                            else if (flag_choice == 1)
                            {
                                Console.WriteLine($"Enter quantity:");
                                int quantity;
                                if (int.TryParse(Console.ReadLine(), out quantity))
                                {
                                    if (quantity > 0 && quantity * cost_dummy <= balance)
                                    {
                                        balance -= (quantity * cost_dummy);
                                        Console.WriteLine("Here's the flag: m365{bogus_flag}");
                                        Console.WriteLine("This is not the one to be submitted, of course. :)");
                                    }
                                    else
                                    {
                                        Console.WriteLine("Insufficient funds. Looks like we have similar bank accounts.");
                                    }
                                }
                                else
                                {
                                    Console.WriteLine("Not int. Try again.");
                                    continue;
                                }
                            }
                            else
                            {
                                Console.WriteLine("Wrong choice. Try again.");
                                continue;
                            }
                        }
                        else
                        {
                            Console.WriteLine("Not int. Try again.");
                            continue;
                        }
                    }
                    else if (choice == 3)
                    {
                        Console.WriteLine("Good Bye");
                        return;
                    }
                    else
                    {
                        Console.WriteLine("Wrong choice. Try again");
                        continue;
                    }
                }
                else
                {
                    Console.WriteLine("Not int. Try again.");
                    continue;
                }
            }
        }
    }
}