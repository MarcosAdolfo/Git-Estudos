using System;

namespace Aula23
{

    class aula23
    {
        static void Main()
        {
            int[] vetor1 = new int[5];
            int[] vetor2 = new int[5];
            int[] vetor3 = new int[5];
            int[,] matriz = new int[2,5]{{11,22,00,44,55},{66,77,88,99,00}};

            Random random = new Random();
            for(int i = 0; i < vetor1.Length; i++)
            {
                vetor1[1] = random.Next(50);
            }
            Console.WriteLine("Elementos do vetor1");
            foreach(int n in vetor1)
            {
                Console.WriteLine(n);
            }

            //public static int BinarySearch(array,valor);
            Console.WriteLine("BinarySearch");
            int procurando = 33;
            int pos = Array.BinarySearch(vetor1,procurando);// Vai retorna a posição do valor a ser procurador
            Console.WriteLine("Valor {0} está na posição {1}",procurando,pos);
            Console.WriteLine("============================================");

            //public static void Copy(Ar_origem,Ar_destino,qtde_elementos);
            Console.WriteLine("Copy");// Copia os valores de um array para outro
            Array.Copy(vetor1,vetor2,vetor1.Length);//array 1, array 2, e a quantidade de elementos ase copiado
            foreach(int n in vetor2)
            {
                Console.WriteLine(n);
            }
            Console.WriteLine("============================================");

            //public void CopyTo(Ar_destino,a_partir_desta_pos);
            Console.WriteLine("CopyTo");// Copia a partir do vetor de origem 
            vetor1.CopyTo(vetor3,0);// os elementos do vetor1 vão ser copiado para o vetor3 a parti do elemento 0
            foreach(int n in vetor3)
            {
                Console.WriteLine(n);
            }
            Console.WriteLine("============================================");

            //public log GetLongLength(dimensão);
            Console.WriteLine("GetLongLength");
            long qtdeElementosVetor = vetor1.GetLongLength(0);
            Console.WriteLine("Quantidade de elementos {0}", qtdeElementosVetor);
            Console.WriteLine("============================================");

            //public int GetLowerBound(dimensão);
            Console.WriteLine("GetLowerBound"); //retorna o meno indice
            int MenorIndiceVetor = vetor1.GetLowerBound(0);
            int MenorIndiceMatriz_D1 = matriz.GetLowerBound(1);
            Console.WriteLine("Menor Indice do vetor1 {0}", MenorIndiceVetor);
            Console.WriteLine("============================================");
            
            //public int GetUpperBound(dimensão);
            Console.WriteLine("GetUpperBound");// retorna o maior indice
            int MaiorIndiceVetor = vetor1.GetUpperBound(0);
            int MaiorIndiceMatriz_D1 = matriz.GetUpperBound(1);
            Console.WriteLine("Maior Indice do vetor1 {0}",MaiorIndiceVetor);
            Console.WriteLine("============================================");

            //public object GetValue(long indice);
            Console.WriteLine("GetValue");
            int valor0 = Convert.ToInt32(vetor1.GetValue(3)); //retorna o valo do indice 3
            int valor1 = Convert.ToInt32(matriz.GetValue(1,3));
            Console.WriteLine("Valor da posição 3 do vetor1: {0}", valor0);
            Console.WriteLine("============================================");

            //public static int IndexOf(array,valor);
            Console.WriteLine("IndexOf"); // retorna o primeiro indice onde um valor apareceu
            int indice1 = Array.IndexOf(vetor1,3); // vai retorna o primeiro indice onde o numero 3 a parece
            Console.WriteLine("Indice do primeiro valor 3:{0}",indice1);
            Console.WriteLine("============================================");

            //public static int LasIndexOf(array,valor);
            Console.WriteLine("LasIndexOf");// faz a mesma coisa do IndexOf so que retorna o ultimo indice onde o valor a pareceu
            int indice2 = Array.LastIndexOf(vetor1,3);
            Console.WriteLine("Indice do Ultimo valor 3:{0}",indice2);
            Console.WriteLine("============================================");

            //public static void Reverse(array);
            Array.Reverse(vetor1); // inverte os valores do array
            foreach(int n in vetor1)
            {
                Console.WriteLine(n);
            }

            //public void SetValue(object valor, long pos);
            vetor2.SetValue(99,0); // seta um valor para uma posição especifica 
            for(int i = 0; i < vetor2.Length; i++)
            {
                vetor2.SetValue(0,i);
            }
            Console.WriteLine("Vetor 2");
            foreach(int n in vetor2)
            {
                Console.WriteLine(n);
            }

            //public static void Sort(array);
            Array.Sort(vetor1); // ordena os valores em ordem crescente
            Array.Sort(vetor2); // para ordena em ordem decrescente usa um Reverse depois
            Array.Sort(vetor3);
            Console.WriteLine("Vetor1");
            foreach(int n in vetor1)
            {
                Console.WriteLine(n);
            }
            Console.WriteLine("\nVetor2");
            foreach(int n in vetor2)
            {
                Console.WriteLine(n);
            }
            Console.WriteLine("\nVetor3");
            foreach(int n in vetor3)
            {
                Console.WriteLine(n);
            }
        }
    }

}