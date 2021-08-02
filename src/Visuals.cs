using System;
using System.Threading;

class Visuals
{
    public static void Header()
    {
        String[] i = new String[4];
        i[0] = "\n**THE PLAINS: REBOOT**************";
        i[1] = "**MADE BY DRAUMAZ IN 2021*********";
        i[2] = "**WRITTEN IN C#!******************";
        i[3] = "**CHARACTER DESIGN BY BRYCE CANO**\n";
        foreach (String s in i)
        {
            Console.WriteLine(s);
        }
    }
    public static void Exit_Header()
    {
        String url = "https://github.com/draumaz/plains-reboot";
        Tools.Clear_Screen();
        Console.WriteLine("\nThanks for playing my game!");
        Tools.Snooze(500);
        Console.Write("\nKeep up with development at ");
        Read_Looper(url, 10);
        Console.Write(".\n");
        Tools.Snooze(200);
    }
    public static void Read_Looper(String s, int speed)
    {
        String[] x = Tools.String_Array_Inator(s);
        for (int i = 0; i < x.Length; i++)
        {
            Console.Write(x[i]);
            Tools.Snooze(speed);
        }
    }
}