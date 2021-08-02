using System;

class Ultravisor
{
    public static void Ultrablade()
    {
        Tools.Clear_Screen();
        Visuals.Header();
        Console.WriteLine("PLAY [1]\nRESET [2]\nQUIT [3]\n");
        Tools.User_Input(1, 5);
    }
}