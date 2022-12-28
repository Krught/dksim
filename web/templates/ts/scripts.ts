function testadd() {
  const ringsubdiv = document.getElementById("all_sort_mh");
      for (var i in mh_name){
        var a = mh_name[i];
        var ia = mh_heroicnum[i];
        var iaa = mh_phasenum[i];
        var child = document.createElement("div");
        child.id = a;
        var namechild = document.createElement("div");
        var heroicchild = document.createElement("div");
        var phasechild = document.createElement("div");
        namechild.innerText = a;
        namechild.className = "nam";
        heroicchild.innerText = ia;
        heroicchild.classList = "heroic";
        phasechild.innerText = iaa;
        phasechild.classList = "phase";
        child?.appendChild(namechild);
        child?.appendChild(heroicchild);
        child?.appendChild(phasechild);
        ringsubdiv?.appendChild(child);
      }
}

testadd();