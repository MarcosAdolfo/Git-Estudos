using System;

namespace Aula25
{

    class aula25
    {
        static void Main()
        {
            int num = 10;
            dobrar(ref num);// usa a variavel por referencia
            Console.WriteLine(num);
        }

        static void dobrar(ref int valor)// quando o valo for trocado na var de ref ela troca o valo na var original
        {
            valor *= 2;
        }
    }

}