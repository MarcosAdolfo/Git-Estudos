using System;

namespace M_Test
{
    
    class Calc
    {
        public double calcular(double x, double y, char operacao)
        {
            double resutado = 0;

            switch (operacao)
            {
                case '+':
                    resutado = (x + y);
                    break;
                case '-':
                    resutado = (x - y);
                    break;
                case '*':
                    resutado = (x * y);
                    break;
                case '/':
                    resutado = (x / y);
                    break;
            }

            return resutado;
        }
    }

    class calculadora
    {
        static void Main()
        {
            Calc calculo = new Calc();

            double x,y = 0;
            char operador = '+';
            string opc = "";
            double resutado = 0;

            Console.WriteLine("Calculadora");

            x = double.Parse(input("Num: "));
            Console.Clear();

            do
            {
                
                operador = char.Parse(input("Escolha um Operador:\n| + | - | * | / |\n:"));
                Console.Clear();

                y = double.Parse(input("Num: "));
                Console.Clear();

                resutado = calculo.calcular(x,y,operador);
                Console.WriteLine("Resutado:\n| {0} |",resutado);
                
                //ATENÇÂO!!!!!!!!!!!!!!!!!!!!!
                do
                {
                    opc = input("[Ente] - para continua a conta.\n[N] - Para nova conta,\n[X] - Para Sair.\n:");
                    if(opc == "" || opc == " ")
                    {
                        x = resutado;
                    }
                    else if(opc == "N"|| opc == "n")
                    {
                        x = double.Parse(input("Num: "));
                    }
                }while(true);
                
                
            }while(opc == "X" || opc == "x");
        }

        static string input(string txt)
        {
            Console.Write(txt);
            return Console.ReadLine();
        }
    }

}