function testadd() {
    var ringsubdiv = document.getElementById("all_sort_mh");
    for (var i in mh_name) {
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
        child === null || child === void 0 ? void 0 : child.appendChild(namechild);
        child === null || child === void 0 ? void 0 : child.appendChild(heroicchild);
        child === null || child === void 0 ? void 0 : child.appendChild(phasechild);
        ringsubdiv === null || ringsubdiv === void 0 ? void 0 : ringsubdiv.appendChild(child);
    }
}
testadd();
