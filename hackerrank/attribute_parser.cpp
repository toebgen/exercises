// https://www.hackerrank.com/challenges/attribute-parser/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <memory>
using namespace std;


/** Tokenize a line, separated by c (whitespace) */
std::vector<std::string> get_tokens(const std::string& line,
                                    std::string c = " "){
    // cout << "get_tokens(" << line << ")" << endl;
    std::vector<string> tokens;
    std::string intermediate = "";
    for (int i=0; i<line.size(); i++){
        if (line[i] == '\"' || line[i] == '<' || line[i] == '>'){
            continue;  // ignore
        }
        if (c.find(line[i]) != std::string::npos) {
            // TODO Potentially allow whitespaces in value string...
            tokens.push_back(intermediate);
            intermediate = "";
        } else {
            intermediate += line[i];
        }
    }
    if (intermediate.size()>0) {
        tokens.push_back(intermediate);
    }
    return tokens;
}

std::string vector_as_string(const std::vector<std::string> vec){
    std::string str = "[";
    for (auto el : vec)
        str += el + ", ";
    return str + "]";
}

void print_map(const std::map<std::string, std::string>& map){
    for (const auto el : map){
        cout << el.first << "=" << el.second << ", ";
    }
}

struct Tag {
    Tag() : tag_name("Dummy"), parent(nullptr){}

    /** Parse information from tokens into member variables */
    void parse_tokens(const std::vector<std::string>& tokens){
        tag_name = tokens[0];  // first one is tag_name
        std::string key, value;
        for (auto it = ++tokens.begin(); it != tokens.end(); it++){
            if (*it == "=") continue;
            if (key.empty()) {
                key = *it;
            } else {
                value = *it;
                attributes.emplace(key, value);
                key.clear();
                value.clear();
            }
        }
    }

    /** Parse a line by first tokenizing it. */
    void parse_line(const std::string& line) {
        auto tokens = get_tokens(line, " ");
        parse_tokens(tokens);
    }

    /** Returns child with given child_tag_name, nullptr otherwise */
    std::shared_ptr<Tag> has_child(const std::string& child_tag_name) {
        for (auto child : children){
            if (child->tag_name == child_tag_name){
                return child;
            }
        }
        return nullptr;
    }

    void print(const std::string& prefix = "") const {
        cout << prefix << tag_name << " (";
        print_map(attributes);
        cout << "): " << endl;
        for (const auto child : children){
            child->print(prefix+"\t");
        }
    }

    std::string tag_name;
    std::map<std::string, std::string> attributes;
    std::vector<std::shared_ptr<Tag>> children;
    std::shared_ptr<Tag> parent;
};

using TagPtr = std::shared_ptr<Tag>;

struct Query {
    void perform(TagPtr root) {
        // cout << endl << "Performing query " << line_str << ", tag_names=" << vector_as_string(tag_names) << endl;
        
        // cout << "Searching query.tag_names=" << vector_as_string(tag_names) << endl;
        for (auto query_tag_name : tag_names){
            // cout << "query_tag_name=" << query_tag_name << ": ";
            TagPtr child = root->has_child(query_tag_name);
            if (child != nullptr){
                root = child;
                // cout << "has child " << child->tag_name << endl;
                // cout << "Continuing searching query.tag_names=" << vector_as_string(tag_names) << endl;
            } else {
                cout << "Not Found!" << endl;
                return;
            }
        }
        auto it = root->attributes.find(attribute);
        if (it != root->attributes.end())
            cout << root->attributes[attribute] << endl;
        else
            cout << "Not Found!" << endl;
        return;
    }

    void parse(const std::string& line) {
        line_str = line;
        std::string::size_type n=0, n_prev=0;
        
        while(n != std::string::npos){
            n_prev = n;
            n = line.find(".", n+1);
            if (n == std::string::npos){
                // no "." found, look for "~" now!
                n = line.find("~", n_prev);
                if (line[n_prev] == '.') n_prev += 1;
                std::string tag_name = line.substr(n_prev, n-n_prev);
                tag_names.push_back(tag_name);
                attribute = line.substr(n+1);
                break;
            } else {
                if (line[n_prev] == '.') n_prev += 1;
                std::string tag_name = line.substr(n_prev, n-n_prev);
                tag_names.push_back(tag_name);
            }
        }
    }

    void print() const {
        cout << line_str << ", tag_names: " << vector_as_string(tag_names);
        cout << "attribute: " << attribute << endl;
    }

    std::vector<std::string> tag_names;
    std::string attribute;
    std::string line_str;
};

TagPtr go_to_root(TagPtr ptr) {
    while(ptr->parent)
        ptr = ptr->parent;
    return ptr;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, Q;
    cin >> N >> Q;

    std::vector<TagPtr> top_level_tags;

    std::string line_str;
    std::getline(std::cin, line_str);
    TagPtr dummy = std::make_shared<Tag>();
    TagPtr current = dummy;
    for (auto line_i=0; line_i<N+Q; line_i++){
        line_str = "";
        std::getline(std::cin, line_str);
        if (line_str.find("</") == 0){
            // end tag: set current pointer to parent, if available
            if(current->parent){
                current = current->parent;
            }
        } else if (line_str.find("<") == 0){
            // start tag: Create a new Tag, add to current->children
            TagPtr new_tag = std::make_shared<Tag>();
            new_tag->parse_line(line_str);
            if(current) {
                // Already working on a Tag,
                // hence add this to its children, set current as new's parent
                new_tag->parent = current;
                current->children.push_back(new_tag);
                current = new_tag;
            } else {
                // First tag ever
                top_level_tags.push_back(new_tag);
                current = new_tag;
            }
        } else {
            // Must be a query
            // Set TagPtr to root
            TagPtr root = current;
            while(root->parent)
                root = root->parent;
            Query query;
            query.parse(line_str);
            // query.print();
            query.perform(root);
        }
    }

    // TagPtr ptr = go_to_root(current);
    // ptr->print();

    return 0;
}
