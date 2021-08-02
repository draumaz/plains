using System;
using System.Linq;
using System.Threading;

class Tools
{
    public static void Clear_Screen()
    {
        Console.Clear();
    }
    public static String[] String_Array_Inator(String i)
    {
        return i.ToCharArray().Select(c => c.ToString()).ToArray();
    }
    public static void Snooze(int ms)
    {
        Thread.Sleep(ms);
    }
    public static void User_Input(int min, int max)
    {
        String Raw_Input;
        int Clean_Input;
        while (true)
        {
            Visuals.Read_Looper("ACTION >> ", 4);
            try
            {
                Raw_Input = Console.ReadLine();
                Clean_Input = Convert.ToInt32(Raw_Input);
                if (Clean_Input < min || Clean_Input > max)
                {
                    if (Clean_Input == 69 || Clean_Input == 420)
                    {
                        Console.WriteLine("\nBased.");
                        Tools.Snooze(500);
                    }
                    else
                    {
                        User_Input_Catch();
                    }
                }
                continue;
            }
            catch (System.FormatException)
            {
                User_Input_Catch();
                continue;
            }
        }
    }
    public static void User_Input_Catch()
    {
        Console.WriteLine("\nDid you mean something else?\n");
        Snooze(150);
    }
}