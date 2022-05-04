﻿using System;
using System.Threading;

namespace Stopwatch
{

    class Program
    {
        static void Main()
        {
            Menu();
        }

        static void Menu()
        {
            Console.Clear();
            Console.WriteLine("S = Segundos => 10s = 10 segundos\nM = Minutos => 1m = 1 Minuto\n0 = Sair");
            Console.Write("Tempo: ");

            string data = Console.ReadLine().ToLower();
            char type = char.Parse(data.Substring(data.Length-1,1));
            int time = int.Parse(data.Substring(0,data.Length-1));
            int multiplier = 1;

            if(type == 'm')
                multiplier = 60;
            if(time == 0)
            {
                Console.Clear();
                System.Environment.Exit(0);
            }
            
            PreStart(time * multiplier);
        }

        static void PreStart(int time)
        {
            Console.Clear();
            Console.WriteLine("Ready...");
            Thread.Sleep(1000);
            Console.WriteLine("Set...");
            Thread.Sleep(1000);
            Console.WriteLine("Go...");
            Thread.Sleep(500);

            Start(time);
        }

        static void Start(int time)
        {
            int currentTime = 0;

            while(currentTime != time)
            {
                Console.Clear();
                currentTime++;
                Console.WriteLine(currentTime);
                Thread.Sleep(1000);
            }

            Console.Clear();
            Console.WriteLine("Stopwatch Finalizado...");
            Thread.Sleep(2500);
            Menu();
        }
    }

}
