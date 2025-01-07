#pragma once
#include <vector>
#include <string>
#include <map>


class WordFilter {
    private:
        std::vector<std::string> significant_words;

    public:
        WordFilter() {

        }

        std::map<std::string, double> getScoreFromPhrase(std::string phrase) {

        }
};