using System;

namespace M_Test
{

    class MutiplasEscolhas
    {
        static void Main()
        {
            string ops;
            Console.WriteLine("Bem Vindo!!!\n[Enter] Para Continua");
            Console.ReadLine();

            do{
                Console.Clear();
                Console.Write("Escolha Uma Opção\n0 - Sai\n1 - entra\n>>> ");
                ops = Console.ReadLine();
                
                switch(ops)
                {
                    case "0":
                    case "sai":
                        Console.Clear();
                        break;
                    case "1":
                        Console.WriteLine("Entrando!");
                        break;
                    default:
                        Console.Write("Opção Invalida!!!\n[Enter] Para Continua");
                        Console.ReadLine();
                        break;
                }
                
              }while(ops != "0" && ops != "sai");
            Console.WriteLine("Adeus!!!");
        }
    }

}