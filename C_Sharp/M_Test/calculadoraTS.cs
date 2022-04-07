using System;

namespace M_Test
{

    class calculadoraTs
    {
        static void Main()
        {
            char operador;
            bool lop = true;

            Console.Clear();
            Txt("Calculadora");
            do{
                Console.WriteLine("Escolha uma opção a baixo:");
                Console.Write("[ + ] - soma\n[ - ] - subitração\n[ * ] - mutiplicação\n[ / ] - divisão\n[ X ] - Par Sair\n>>>");
                operador = char.Parse(Console.ReadLine());
                Console.Clear(); 
                switch(operador)
                {
                    case '+':
                        Txt("+++ Soma +++");
                        Console.WriteLine("Total da Soma: {0}\n",Soma());
                        break;

                    case '-':
                        Txt("--- Subitração ---");
                        Console.WriteLine("Total da Subitração: {0}\n",Subitracao());
                        break;

                    case '*':
                        Txt("*** Mutiplicação ***");
                        Console.WriteLine("Total da Mutiplicação: {0}\n",Mutiplicacao());
                        break;

                    case '/':
                        Txt("/// Divisão ///");
                        Console.WriteLine("Total da Divisão: {0}\n",Divisao());
                        break;

                    case 'X':
                    case 'x':
                        lop = false;
                        break;

                    default:
                        Console.WriteLine("Opção invalida!!!");
                        break;
                }
            }while(lop);
        }

        //Texto

        static void Txt(string txt)
        {
            Console.WriteLine("==============================");
            Console.WriteLine(string.Format("{0,20}",txt));
            Console.WriteLine("==============================");
        }

        //Soma

        static float Soma()
        {
            float tot=0,val = 0;
            int cont = 0;

            Console.WriteLine("Todos os numeros digitados serão somados\n[ 0 ] - para sair");

            do{
                cont++;
                Console.Write("Digite o {0}° numero: ",cont);
                val = float.Parse(Console.ReadLine());
                tot += val;
            }while(val != 0);

            Console.Clear();
            Console.WriteLine("Foram Somados {0} numeros",cont-1);

            return tot;
        }

        //Subitração

        static float Subitracao()
        {
            float tot=0,val = 0;
            int cont = 0;

            Console.WriteLine("Todos os numeros digitados serão subitraidos\n[ 0 ] - para sair");

            do{
                cont++;
                Console.Write("Digite o {0}° numero: ",cont);
                val = float.Parse(Console.ReadLine());
                tot -= val;
            }while(val != 0);

            Console.Clear();
            Console.WriteLine("Foram Subitraidos {0} numeros",cont-1);

            return tot;
        }

        //Mutiplicação

        static float Mutiplicacao()
        {
            float tot=1,val = 1;
            int cont = 0;

            Console.WriteLine("Todos os numeros digitados serão mutiplicados\n[ 0 ] - para sair");

            do{
                cont++;
                tot *= val;
                Console.Write("Digite o {0}° numero: ",cont);
                val = float.Parse(Console.ReadLine());
            }while(val != 0);

            Console.Clear();
            Console.WriteLine("Foram Mutiplicados {0} numeros",cont-1);

            return tot;
        }

        //Divisão

        static float Divisao()
        {
            float tot=1,val = 1;
            int cont = 0;

            Console.WriteLine("Todos os numeros digitados serão divididos\n[ 0 ] - para sair");

            cont++;
            Console.Write("Digite o {0}° numero: ",cont);
            tot = float.Parse(Console.ReadLine());

            do{
                cont++;
                tot /= val;
                Console.Write("Digite o {0}° numero: ",cont);
                val = float.Parse(Console.ReadLine());
            }while(val != 0);

            Console.Clear();
            Console.WriteLine("Foram Divididos {0} numeros",cont-1);

            return tot;
        }
    }

}