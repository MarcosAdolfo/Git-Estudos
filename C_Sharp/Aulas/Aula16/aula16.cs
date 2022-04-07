using System; 

namespace Aula15
{

    class aula15
    {
        static void Main()
        {
            int tempo = 0;
            char escolha;

            inicio:

            Console.Clear();

            Console.WriteLine("BH a Vitoria/ES");
            Console.WriteLine("Escolha o transporte:\n [a]-Avião\n [c]-Carro\n [o]-Ônibus");
            
            escolha = char.Parse(Console.ReadLine());

            switch(escolha)
            {
                case 'a':
                case 'A':
                    tempo = 50;
                    break;
                case 'c':
                    tempo = 480;
                    break;
                case 'o':
                    tempo = 660;
                    break;
                default:
                    tempo = -1;
                    break;
            }

            if(tempo < 0)
            {
                Console.WriteLine("Tramsporte indisponível");
            }
            else
            {
                Console.WriteLine("Para o Tramsporte escolhido o tempo é: {0}m", tempo);
            }

            Console.Write("\nCalcula outro Tramsporte?[s/n]");
            escolha = char.Parse(Console.ReadLine());
            if(escolha == 's' || escolha == 'S')
            {
                goto inicio;
            }
            else
            {
                Console.Clear();
                Console.WriteLine("Fim do programa");
            }

        }
    }

}