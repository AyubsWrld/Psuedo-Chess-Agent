#! /usr/bin/perl
use FileHandle;
use IPC::Open2;

if($#ARGV!=1)
{
  print "USAGE: td.pl blackplayer whiteplayer\n"; 
}
else
{

for($i=1;$i<=1;$i++){

  system("rm -f .newgame.txt");
  system("rm -f .history.txt");

  $aaa = "echo \"BXBXBXBXB\nXBXBXBXBX\">>.newgame.txt";
  system($aaa);
  system($aaa);

  $aaa = "echo \"WXWXOXBXB\">>.newgame.txt";
  system($aaa);
  $aaa = "echo \"XWXWXWXWX\nWXWXWXWXW\">>.newgame.txt";
  system($aaa);
  system($aaa);
  $stop=1;
  $bbb="./".$ARGV[0] . " .newgame.txt B>.B";
  $www="./".$ARGV[1] . " .newgame.txt W>.W";
  open(HH, '>', ".history$i.txt");
  $cons=0;

  while($stop!=0)
  {
    system($bbb);
    open(FH, '<', ".B");
    $ll = <FH>;
    $ll=substr($ll,0,-1);
    close(FH);
    $aaa = "./expmovecheck .newgame.txt B " . $ll;
    system($aaa);
    if($?!=0) {close(HH);exit()};
    
    open(FH, '<', ".Type");
    $aa= <FH>;
    close(FH);

    if ($aa eq "1")
    {
      $cons=$cons+1;
      $tt="move";
    }
    else
    {
      $cons=0;
      $tt="capture";
    }
    $bl="B:". $ll. " Type:". $tt ."\n";;
    print $bl;
    print HH $bl;
    if ($cons==20)  {close(HH);print("GAME OVER: TIE\n");exit()};

    system($www);
    open(FH, '<', ".W");
    $ll=<FH>;
    $ll=substr($ll,0,-1);
    close(FH);
    $aaa = "./expmovecheck .newgame.txt W " . $ll;
    system($aaa); 
    if($?!=0) {close(HH);exit()};

    open(FH, '<', ".Type");
    $aa = <FH>;
    close(FH);
    if ($aa eq "1")
    {
      $cons=$cons+1;
      $tt="move";
    }
    else
    {
      $cons=0;
      $tt="capture";
    }
    if ($cons==20)  {close(HH);print("GAME OVER: TIE\n");exit()};

    $wl="W:". $ll. " Type:" . $tt ."\n";
    print$wl;
    print HH $wl;
  }    
#system("rm -f .newgame.txt"); 
}
}
