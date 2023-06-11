#include <iostream>
#include <vector>
main(){
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }
    for (const auto& l : lines) {
        std::cout << l << std::endl;
    }
}
