using System;

namespace M_Test
{

    class Opcao
    {
        public string ops = "";
        int n = 0;
        bool resp = false;
        public bool comparador(params string[]tx)
        {
            if(this.ops == tx[n])
            {
                resp = true;
            }
            else if(n+1 >= tx.Length)
            {
                n=0;
                resp = false;
            }
            else
            {
                n++;
                comparador(tx);
            }
            return resp;
        }
    }

    class calculadoraTS_02
    {
        static void Main()
        {
            double res = 0;

            Opcao op = new Opcao();

            titulo("Calculadora");

            double x = double.Parse(print("Primeiro Numero: "));

            double y = double.Parse(print("Segundo Numero: "));

            do
            {
                Console.Clear();

                Console.WriteLine("Escolha uma operação: ");

                while(!op.comparador("+","-","*","/"))
                {
                    op.ops = print("[ + ] - soma\n[ - ] - subitração\n[ * ] - mutiplicação\n[ / ] - divisão\n>>>");

                    switch(op.ops)
                    {
                        case "+":
                            res = x + y;
                            break;
                        case "-":
                            res = x - y;
                            break;
                        case "*":
                            res = x * y;
                            break;
                        case "/":
                            res = x / y;
                            break;
                        default:
                            Console.Clear();
                            Console.WriteLine("Opção invalida!! Escolha uma opção valida!");
                            break;
                    }

                }

                titulo("Resutado: "+res);

                do
                {
                    op.ops = print("[Enter] - Continua com este numero\n[N] - Nova conta\n[X] - Sair\n>>>");
                    Console.Clear();
                } while (!op.comparador(""," ","N","n","X","x"));

                if(op.ops == "N" || op.ops =="n")
                {
                    x = double.Parse(print("Primeiro Numero: "));
                    y = double.Parse(print("Segundo Numero: "));
                }
                else if(op.ops == " " || op.ops == "")
                {
                    x = res;
                    y = double.Parse(print("Digite um novo numero: "));
                }
                else
                {
                    break;
                }

            } while(true);
        }

        public static void titulo(string txt)
        {
            Console.WriteLine("=======================");
            Console.WriteLine("{0,20}",txt);
            Console.WriteLine("=======================");
        }
        public static string print(string txt)
        {
            Console.Write(txt);
            return Console.ReadLine();
        }

    }

}